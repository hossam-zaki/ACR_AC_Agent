import sys
from io import StringIO
from typing import Any, Dict, List, Tuple

from llama_index.core.agent.types import BaseAgent
from llama_index.core.llama_pack.base import BaseLlamaPack


class Capturing(list):
    """To capture the stdout from `BaseAgent.stream_chat` with `verbose=True`. Taken from
    https://stackoverflow.com/questions/16571150/\
        how-to-capture-stdout-output-from-a-python-function-call.
    """

    def __enter__(self) -> Any:
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self

    def __exit__(self, *args) -> None:
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio  # free up some memory
        sys.stdout = self._stdout


class GradioAgentChatPack(BaseLlamaPack):
    """Gradio chatbot to chat with your own Agent."""

    def __init__(
        self,
        agent: BaseAgent,
        **kwargs: Any,
    ) -> None:
        """Init params."""
        try:
            from ansi2html import Ansi2HTMLConverter
        except ImportError:
            raise ImportError("Please install ansi2html via `pip install ansi2html`")

        self.agent = agent
        self.thoughts = ""
        self.conv = Ansi2HTMLConverter()

    def get_modules(self) -> Dict[str, Any]:
        """Get modules."""
        return {"agent": self.agent}

    def _handle_user_message(self, user_message, history):
        """Handle the user submitted message. Clear message box, and append
        to the history.
        """
        return "", [*history, (user_message, "")]

    def _generate_response(
        self, chat_history: List[Tuple[str, str]]
    ) -> Tuple[str, List[Tuple[str, str]]]:
        """Generate the response from agent, and capture the stdout of the
        ReActAgent's thoughts.
        """
        # with Capturing() as output:
        
        response = self.agent.chat(chat_history[-1][0])
        response.is_dummy_stream = True
        ansi = "\n========\n" + str(response)
        html_output = self.conv.convert(ansi)

        for token in response.response_gen:
            chat_history[-1][1] += token
            yield chat_history, str(html_output)

    def _reset_chat(self) -> Tuple[str, str]:
        """Reset the agent's chat history. And clear all dialogue boxes."""
        # clear agent history
        self.agent.reset()
        return "", "", ""  # clear textboxes

    def run(self, *args: Any, **kwargs: Any) -> Any:
        """Run the pipeline."""
        import gradio as gr
        from gradio.themes.utils import colors, fonts, sizes

        gr.close_all()
        llama_theme = gr.themes.Soft(
            primary_hue=colors.blue,
            secondary_hue=colors.teal,
            neutral_hue=colors.gray,
            spacing_size=sizes.spacing_md,
            radius_size=sizes.radius_md,
            text_size=sizes.text_lg,
            font=(
                fonts.GoogleFont("Quicksand"),
                "ui-sans-serif",
                "sans-serif",
            ),
            font_mono=(
                fonts.GoogleFont("IBM Plex Mono"),
                "ui-monospace",
                "monospace",
            ),
        )
        llama_theme.set(
            body_background_fill="#F0F4F8",
            body_background_fill_dark="#1E1E1E",
            button_primary_background_fill="linear-gradient(90deg, *primary_400, *secondary_500)",
            button_primary_background_fill_hover="linear-gradient(90deg, *primary_300, *secondary_400)",
            button_primary_text_color="white",
            button_primary_background_fill_dark="linear-gradient(90deg, *primary_700, *secondary_900)",
            slider_color="*secondary_400",
            slider_color_dark="*secondary_700",
            block_title_text_weight="700",
            block_border_width="2px",
            block_shadow="*shadow_drop_md",
            button_large_padding="16px",
        )

        demo = gr.Blocks(
            theme=gr.themes.Soft(),
            css="#box { height: 420px; overflow-y: auto; background-color: #FFFFFF; padding: 10px; border-radius: 8px; } #logo { align-self: center; }",
        )
        with demo:
            with gr.Row():
                gr.Markdown(
                    "<h1 style='text-align:center; font-size:2.5em;'>Interventional Radiology Appropriateness Criteria</h1>",
                    elem_id="header",
                )
            with gr.Row():
                chat_window = gr.Chatbot(
                    label="Message History",
                    scale=3,
                    elem_id="chat_window",
                )
            with gr.Row():
                message = gr.Textbox(label="Write A Message", scale=4, elem_id="input_box", placeholder="Type your message here...")
                clear = gr.ClearButton()

            message.submit(
                self._handle_user_message,
                [message, chat_window],
                [message, chat_window],
                queue=False,
            ).then(
                self._generate_response,
                chat_window,
                [chat_window],
            )
            clear.click(self._reset_chat, None, [message, chat_window])

        demo.launch(server_name="0.0.0.0", server_port=8080)
