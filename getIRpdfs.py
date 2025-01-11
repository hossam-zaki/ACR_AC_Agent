import os
import requests
from bs4 import BeautifulSoup

# Sample HTML (replace with your actual HTML or load from a file)
html_content = """
<div class="panels-div_3 mx-2">

                                
<style>
    .datatableOuter-border {
        border-top: none;
        border-bottom: none;
        border-right: none;
    }

    #style-1::-webkit-scrollbar-track, #style-2::-webkit-scrollbar-track {
        background-color: #fff;
        border-left: 1px solid #b4d0fe;
    }

    .scrollBox {
        border: 1px solid #b4d0fe !important;
        border-left: none;
        position: relative;
        background: #fff;
        overflow-y: auto;
    }

    .scrollBox-inner {
        max-height: calc(100vh - (420px));
    }

    .priorityClinicalAreas {
        list-style-type: square;
        padding-left: 5%;
    }

    .font-size-15px {
        font-size: 12px;
    }

    .topicHeading {
        color: rgb(20, 95, 169);
        font-weight: bold;
    }

    .padding-left-4 {
        padding-left: 4%;
    }

    .divOdd {
        background: #F2F2F2 !important;
    }

    .divEven {
        background: #fff !important;
    }

    .headerColor {
        color: rgb(20, 95, 169);
    }

    .divPanelName {
        border-top: 1px solid #ddd;
        border-bottom: 1px solid #ddd;
    }

    .pcas {
        border-radius: 14px;
        position: relative;
        background-color: #1b81c2;
        color: #fff !important;
        border: solid 1px #1b81c2;
        padding: 5px 10px;
    }
</style>
<div class="scrollBox divListPage mb-2" id="style-1">
    <div class="scrollBox-inner">
        <div class="">

            <div class="form-group table datatable-columns bg-white dataTable no-footer">
                        <div class="col-lg-12 p-2 divPanelName">
                            <h2 class="m-0 headerColor">Interventional Radiology</h2>
                        </div>
                                <div class="p-2 row divEven">
                                    <div class="col-lg-4">
Abdominal Aortic Aneurysm or Dissection-Interventional Planning and Follow-up
                                    </div>

                                    <div class="col-lg-8">
                                        <div class="row">
                                            <div class="col-lg-3">
                                                    <a href="/docs/70548/Narrative/" target="_blank" class="download-pdf-icon2"></a>
<a class="wordwrap downloadLink" href="/docs/70548/Narrative/" target="_blank">Narrative &amp; Rating Table</a>                                            </div>
                                            <div class="col-lg-2">
                                                <a href="/docs/70548/EvidenceTable/" target="_blank" class="download-pdf-icon2"></a>
                                                <a class="wordwrap downloadLink" href="/list/GetEvidence?TopicId=174&amp;TopicName=Abdominal%20Aortic%20Aneurysm%20or%20Dissection-Interventional%20Planning%20and%20Follow-up" target="_blank">Evidence Table</a>
                                            </div>
                                            <div class="col-lg-2">
                                                    <a href="/docs/70548/LitSearch/" target="_blank" class="download-pdf-icon2"></a>
<a class="wordwrap downloadLink" href="/docs/70548/LitSearch/" target="_blank">Lit Search</a>                                            </div>
                                            <div class="col-lg-2">
                                                <a href="/list/GenerateAppendixPDF?TopicId=174&amp;PanelName=Interventional Radiology" class="download-pdf-icon2" target="_blank" title="Click here to download"></a>
                                                <a href="/list/GetAppendix?TopicId=174&amp;PanelName=Interventional Radiology" title="Click here to download" target="_blank" class="wordwrap downloadLink">Appendix</a>
                                            </div>

                                            <div class="col-lg-3">
                                                    <a href="https://www.jacr.org/article/S1546-1440(20)30251-9/pdf" class="link-icon downloadLink" target="_blank" title="Patient Summary">Patient Summary</a>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="p-2 row divOdd">
                                    <div class="col-lg-4">
Central Venous Access Device and Site Selection
                                    </div>

                                    <div class="col-lg-8">
                                        <div class="row">
                                            <div class="col-lg-3">
                                                    <a href="/docs/3094281/Narrative/" target="_blank" class="download-pdf-icon2"></a>
<a class="wordwrap downloadLink" href="/docs/3094281/Narrative/" target="_blank">Narrative &amp; Rating Table</a>                                            </div>
                                            <div class="col-lg-2">
                                                <a href="/docs/3094281/EvidenceTable/" target="_blank" class="download-pdf-icon2"></a>
                                                <a class="wordwrap downloadLink" href="/list/GetEvidence?TopicId=222&amp;TopicName=Central%20Venous%20Access%20Device%20and%20Site%20Selection" target="_blank">Evidence Table</a>
                                            </div>
                                            <div class="col-lg-2">
                                                    <a href="/list/ViewSearchStrategy?ReleaseId=103&amp;TopicId=222&amp;LitReviewID=234" target="_blank" class="download-pdf-icon2"></a>
                                                    <a href="/list/ViewSearchStrategy?ReleaseId=103&amp;TopicId=222&amp;LitReviewID=234" class="wordwrap downloadLink" target="_blank">Lit Search</a>
                                            </div>
                                            <div class="col-lg-2">
                                                <a href="/list/GenerateAppendixPDF?TopicId=222&amp;PanelName=Interventional Radiology" class="download-pdf-icon2" target="_blank" title="Click here to download"></a>
                                                <a href="/list/GetAppendix?TopicId=222&amp;PanelName=Interventional Radiology" title="Click here to download" target="_blank" class="wordwrap downloadLink">Appendix</a>
                                            </div>

                                            <div class="col-lg-3">
                                                    <a href="https://www.jacr.org/article/S1546-1440(23)00201-6/pdf" class="link-icon downloadLink" target="_blank" title="Patient Summary">Patient Summary</a>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="p-2 row divEven">
                                    <div class="col-lg-4">
Dialysis Fistula Malfunction 
                                    </div>

                                    <div class="col-lg-8">
                                        <div class="row">
                                            <div class="col-lg-3">
                                                    <a href="/docs/3158170/Narrative/" target="_blank" class="download-pdf-icon2"></a>
<a class="wordwrap downloadLink" href="/docs/3158170/Narrative/" target="_blank">Narrative &amp; Rating Table</a>                                            </div>
                                            <div class="col-lg-2">
                                                <a href="/docs/3158170/EvidenceTable/" target="_blank" class="download-pdf-icon2"></a>
                                                <a class="wordwrap downloadLink" href="/list/GetEvidence?TopicId=291&amp;TopicName=Dialysis%20Fistula%20Malfunction%20" target="_blank">Evidence Table</a>
                                            </div>
                                            <div class="col-lg-2">
                                                    <a href="/list/ViewSearchStrategy?ReleaseId=103&amp;TopicId=291&amp;LitReviewID=181" target="_blank" class="download-pdf-icon2"></a>
                                                    <a href="/list/ViewSearchStrategy?ReleaseId=103&amp;TopicId=291&amp;LitReviewID=181" class="wordwrap downloadLink" target="_blank">Lit Search</a>
                                            </div>
                                            <div class="col-lg-2">
                                                <a href="/list/GenerateAppendixPDF?TopicId=291&amp;PanelName=Interventional Radiology" class="download-pdf-icon2" target="_blank" title="Click here to download"></a>
                                                <a href="/list/GetAppendix?TopicId=291&amp;PanelName=Interventional Radiology" title="Click here to download" target="_blank" class="wordwrap downloadLink">Appendix</a>
                                            </div>

                                            <div class="col-lg-3">
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="p-2 row divOdd">
                                    <div class="col-lg-4">
Lower Extremity Chronic Venous Disease
                                    </div>

                                    <div class="col-lg-8">
                                        <div class="row">
                                            <div class="col-lg-3">
                                                    <a href="/docs/69507/Narrative/" target="_blank" class="download-pdf-icon2"></a>
<a class="wordwrap downloadLink" href="/docs/69507/Narrative/" target="_blank">Narrative &amp; Rating Table</a>                                            </div>
                                            <div class="col-lg-2">
                                                <a href="/docs/69507/EvidenceTable/" target="_blank" class="download-pdf-icon2"></a>
                                                <a class="wordwrap downloadLink" href="/list/GetEvidence?TopicId=165&amp;TopicName=Lower%20Extremity%20Chronic%20Venous%20Disease" target="_blank">Evidence Table</a>
                                            </div>
                                            <div class="col-lg-2">
                                                    <a href="/list/ViewSearchStrategy?ReleaseId=103&amp;TopicId=165&amp;LitReviewID=100" target="_blank" class="download-pdf-icon2"></a>
                                                    <a href="/list/ViewSearchStrategy?ReleaseId=103&amp;TopicId=165&amp;LitReviewID=100" class="wordwrap downloadLink" target="_blank">Lit Search</a>
                                            </div>
                                            <div class="col-lg-2">
                                                <a href="/list/GenerateAppendixPDF?TopicId=165&amp;PanelName=Interventional Radiology" class="download-pdf-icon2" target="_blank" title="Click here to download"></a>
                                                <a href="/list/GetAppendix?TopicId=165&amp;PanelName=Interventional Radiology" title="Click here to download" target="_blank" class="wordwrap downloadLink">Appendix</a>
                                            </div>

                                            <div class="col-lg-3">
                                                    <a href="https://www.jacr.org/article/S1546-1440(24)00846-9/pdf" class="link-icon downloadLink" target="_blank" title="Patient Summary">Patient Summary</a>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="p-2 row divEven">
                                    <div class="col-lg-4">
Management of Iliac Artery Occlusive Disease
                                    </div>

                                    <div class="col-lg-8">
                                        <div class="row">
                                            <div class="col-lg-3">
                                                    <a href="/docs/69341/Narrative/" target="_blank" class="download-pdf-icon2"></a>
<a class="wordwrap downloadLink" href="/docs/69341/Narrative/" target="_blank">Narrative &amp; Rating Table</a>                                            </div>
                                            <div class="col-lg-2">
                                                <a href="/docs/69341/EvidenceTable/" target="_blank" class="download-pdf-icon2"></a>
                                                <a class="wordwrap downloadLink" href="/list/GetEvidence?TopicId=5&amp;TopicName=Management%20of%20Iliac%20Artery%20Occlusive%20Disease" target="_blank">Evidence Table</a>
                                            </div>
                                            <div class="col-lg-2">
                                                    <a href="/list/ViewSearchStrategy?ReleaseId=103&amp;TopicId=5&amp;LitReviewID=239" target="_blank" class="download-pdf-icon2"></a>
                                                    <a href="/list/ViewSearchStrategy?ReleaseId=103&amp;TopicId=5&amp;LitReviewID=239" class="wordwrap downloadLink" target="_blank">Lit Search</a>
                                            </div>
                                            <div class="col-lg-2">
                                                <a href="/list/GenerateAppendixPDF?TopicId=5&amp;PanelName=Interventional Radiology" class="download-pdf-icon2" target="_blank" title="Click here to download"></a>
                                                <a href="/list/GetAppendix?TopicId=5&amp;PanelName=Interventional Radiology" title="Click here to download" target="_blank" class="wordwrap downloadLink">Appendix</a>
                                            </div>

                                            <div class="col-lg-3">
                                                    <a href="https://www.jacr.org/article/S1546-1440(18)30596-9/pdf" class="link-icon downloadLink" target="_blank" title="Patient Summary">Patient Summary</a>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="p-2 row divOdd">
                                    <div class="col-lg-4">
Management of Liver Cancer
                                    </div>

                                    <div class="col-lg-8">
                                        <div class="row">
                                            <div class="col-lg-3">
                                                    <a href="/docs/69379/Narrative/" target="_blank" class="download-pdf-icon2"></a>
<a class="wordwrap downloadLink" href="/docs/69379/Narrative/" target="_blank">Narrative &amp; Rating Table</a>                                            </div>
                                            <div class="col-lg-2">
                                                <a href="/docs/69379/EvidenceTable/" target="_blank" class="download-pdf-icon2"></a>
                                                <a class="wordwrap downloadLink" href="/list/GetEvidence?TopicId=43&amp;TopicName=Management%20of%20Liver%20Cancer" target="_blank">Evidence Table</a>
                                            </div>
                                            <div class="col-lg-2">
                                                    <a href="/list/ViewSearchStrategy?ReleaseId=103&amp;TopicId=43&amp;LitReviewID=180" target="_blank" class="download-pdf-icon2"></a>
                                                    <a href="/list/ViewSearchStrategy?ReleaseId=103&amp;TopicId=43&amp;LitReviewID=180" class="wordwrap downloadLink" target="_blank">Lit Search</a>
                                            </div>
                                            <div class="col-lg-2">
                                                <a href="/list/GenerateAppendixPDF?TopicId=43&amp;PanelName=Interventional Radiology" class="download-pdf-icon2" target="_blank" title="Click here to download"></a>
                                                <a href="/list/GetAppendix?TopicId=43&amp;PanelName=Interventional Radiology" title="Click here to download" target="_blank" class="wordwrap downloadLink">Appendix</a>
                                            </div>

                                            <div class="col-lg-3">
                                                    <a href="https://www.jacr.org/action/showPdf?pii=S1546-1440%2823%2900262-4" class="link-icon downloadLink" target="_blank" title="Patient Summary">Patient Summary</a>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="p-2 row divEven">
                                    <div class="col-lg-4">
Management of Uterine Fibroids
                                    </div>

                                    <div class="col-lg-8">
                                        <div class="row">
                                            <div class="col-lg-3">
                                                    <a href="/docs/69508/Narrative/" target="_blank" class="download-pdf-icon2"></a>
<a class="wordwrap downloadLink" href="/docs/69508/Narrative/" target="_blank">Narrative &amp; Rating Table</a>                                            </div>
                                            <div class="col-lg-2">
                                                <a href="/docs/69508/EvidenceTable/" target="_blank" class="download-pdf-icon2"></a>
                                                <a class="wordwrap downloadLink" href="/list/GetEvidence?TopicId=166&amp;TopicName=Management%20of%20Uterine%20Fibroids" target="_blank">Evidence Table</a>
                                            </div>
                                            <div class="col-lg-2">
                                                    <a href="/list/ViewSearchStrategy?ReleaseId=103&amp;TopicId=166&amp;LitReviewID=240" target="_blank" class="download-pdf-icon2"></a>
                                                    <a href="/list/ViewSearchStrategy?ReleaseId=103&amp;TopicId=166&amp;LitReviewID=240" class="wordwrap downloadLink" target="_blank">Lit Search</a>
                                            </div>
                                            <div class="col-lg-2">
                                                <a href="/list/GenerateAppendixPDF?TopicId=166&amp;PanelName=Interventional Radiology" class="download-pdf-icon2" target="_blank" title="Click here to download"></a>
                                                <a href="/list/GetAppendix?TopicId=166&amp;PanelName=Interventional Radiology" title="Click here to download" target="_blank" class="wordwrap downloadLink">Appendix</a>
                                            </div>

                                            <div class="col-lg-3">
                                                    <a href="https://www.jacr.org/article/S1546-1440(20)30366-5/pdf" class="link-icon downloadLink" target="_blank" title="Patient Summary">Patient Summary</a>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="p-2 row divOdd">
                                    <div class="col-lg-4">
                                                <span class="topicHeading">Management of Vertebral Compression Fractures</span>
                                                <span class="font-size-15px pcas" title="Cervical or Neck Pain, Low Back Pain">PCAs</span>

                                    </div>

                                    <div class="col-lg-8">
                                        <div class="row">
                                            <div class="col-lg-3">
                                                    <a href="/docs/70545/Narrative/" target="_blank" class="download-pdf-icon2"></a>
<a class="wordwrap downloadLink" href="/docs/70545/Narrative/" target="_blank">Narrative &amp; Rating Table</a>                                            </div>
                                            <div class="col-lg-2">
                                                <a href="/docs/70545/EvidenceTable/" target="_blank" class="download-pdf-icon2"></a>
                                                <a class="wordwrap downloadLink" href="/list/GetEvidence?TopicId=171&amp;TopicName=Management%20of%20Vertebral%20Compression%20Fractures" target="_blank">Evidence Table</a>
                                            </div>
                                            <div class="col-lg-2">
                                                    <a href="/list/ViewSearchStrategy?ReleaseId=103&amp;TopicId=171&amp;LitReviewID=219" target="_blank" class="download-pdf-icon2"></a>
                                                    <a href="/list/ViewSearchStrategy?ReleaseId=103&amp;TopicId=171&amp;LitReviewID=219" class="wordwrap downloadLink" target="_blank">Lit Search</a>
                                            </div>
                                            <div class="col-lg-2">
                                                <a href="/list/GenerateAppendixPDF?TopicId=171&amp;PanelName=Interventional Radiology" class="download-pdf-icon2" target="_blank" title="Click here to download"></a>
                                                <a href="/list/GetAppendix?TopicId=171&amp;PanelName=Interventional Radiology" title="Click here to download" target="_blank" class="wordwrap downloadLink">Appendix</a>
                                            </div>

                                            <div class="col-lg-3">
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="p-2 row divEven">
                                    <div class="col-lg-4">
Radiologic Management of Biliary Obstruction
                                    </div>

                                    <div class="col-lg-8">
                                        <div class="row">
                                            <div class="col-lg-3">
                                                    <a href="/docs/69344/Narrative/" target="_blank" class="download-pdf-icon2"></a>
<a class="wordwrap downloadLink" href="/docs/69344/Narrative/" target="_blank">Narrative &amp; Rating Table</a>                                            </div>
                                            <div class="col-lg-2">
                                                <a href="/docs/69344/EvidenceTable/" target="_blank" class="download-pdf-icon2"></a>
                                                <a class="wordwrap downloadLink" href="/list/GetEvidence?TopicId=8&amp;TopicName=Radiologic%20Management%20of%20Biliary%20Obstruction" target="_blank">Evidence Table</a>
                                            </div>
                                            <div class="col-lg-2">
                                                    <a href="/docs/69344/LitSearch/" target="_blank" class="download-pdf-icon2"></a>
<a class="wordwrap downloadLink" href="/docs/69344/LitSearch/" target="_blank">Lit Search</a>                                            </div>
                                            <div class="col-lg-2">
                                                <a href="/list/GenerateAppendixPDF?TopicId=8&amp;PanelName=Interventional Radiology" class="download-pdf-icon2" target="_blank" title="Click here to download"></a>
                                                <a href="/list/GetAppendix?TopicId=8&amp;PanelName=Interventional Radiology" title="Click here to download" target="_blank" class="wordwrap downloadLink">Appendix</a>
                                            </div>

                                            <div class="col-lg-3">
                                                    <a href="https://www.jacr.org/action/showPdf?pii=S1546-1440%2820%2930678-5" class="link-icon downloadLink" target="_blank" title="Patient Summary">Patient Summary</a>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="p-2 row divOdd">
                                    <div class="col-lg-4">
Radiologic Management of Gastric Varices
                                    </div>

                                    <div class="col-lg-8">
                                        <div class="row">
                                            <div class="col-lg-3">
                                                    <a href="/docs/70911/Narrative/" target="_blank" class="download-pdf-icon2"></a>
<a class="wordwrap downloadLink" href="/docs/70911/Narrative/" target="_blank">Narrative &amp; Rating Table</a>                                            </div>
                                            <div class="col-lg-2">
                                                <a href="/docs/70911/EvidenceTable/" target="_blank" class="download-pdf-icon2"></a>
                                                <a class="wordwrap downloadLink" href="/list/GetEvidence?TopicId=180&amp;TopicName=Radiologic%20Management%20of%20Gastric%20Varices" target="_blank">Evidence Table</a>
                                            </div>
                                            <div class="col-lg-2">
                                                    <a href="/docs/70911/LitSearch/" target="_blank" class="download-pdf-icon2"></a>
<a class="wordwrap downloadLink" href="/docs/70911/LitSearch/" target="_blank">Lit Search</a>                                            </div>
                                            <div class="col-lg-2">
                                                <a href="/list/GenerateAppendixPDF?TopicId=180&amp;PanelName=Interventional Radiology" class="download-pdf-icon2" target="_blank" title="Click here to download"></a>
                                                <a href="/list/GetAppendix?TopicId=180&amp;PanelName=Interventional Radiology" title="Click here to download" target="_blank" class="wordwrap downloadLink">Appendix</a>
                                            </div>

                                            <div class="col-lg-3">
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="p-2 row divEven">
                                    <div class="col-lg-4">
Radiologic Management of Iliofemoral Venous Thrombosis
                                    </div>

                                    <div class="col-lg-8">
                                        <div class="row">
                                            <div class="col-lg-3">
                                                    <a href="/docs/3082663/Narrative/" target="_blank" class="download-pdf-icon2"></a>
<a class="wordwrap downloadLink" href="/docs/3082663/Narrative/" target="_blank">Narrative &amp; Rating Table</a>                                            </div>
                                            <div class="col-lg-2">
                                                <a href="/docs/3082663/EvidenceTable/" target="_blank" class="download-pdf-icon2"></a>
                                                <a class="wordwrap downloadLink" href="/list/GetEvidence?TopicId=193&amp;TopicName=Radiologic%20Management%20of%20Iliofemoral%20Venous%20Thrombosis" target="_blank">Evidence Table</a>
                                            </div>
                                            <div class="col-lg-2">
                                                    <a href="/list/ViewSearchStrategy?ReleaseId=103&amp;TopicId=193&amp;LitReviewID=109" target="_blank" class="download-pdf-icon2"></a>
                                                    <a href="/list/ViewSearchStrategy?ReleaseId=103&amp;TopicId=193&amp;LitReviewID=109" class="wordwrap downloadLink" target="_blank">Lit Search</a>
                                            </div>
                                            <div class="col-lg-2">
                                                <a href="/list/GenerateAppendixPDF?TopicId=193&amp;PanelName=Interventional Radiology" class="download-pdf-icon2" target="_blank" title="Click here to download"></a>
                                                <a href="/list/GetAppendix?TopicId=193&amp;PanelName=Interventional Radiology" title="Click here to download" target="_blank" class="wordwrap downloadLink">Appendix</a>
                                            </div>

                                            <div class="col-lg-3">
                                                    <a href="https://www.jacr.org/article/S1546-1440(24)00678-1/pdf" class="link-icon downloadLink" target="_blank" title="Patient Summary">Patient Summary</a>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="p-2 row divOdd">
                                    <div class="col-lg-4">
Radiologic Management of Infected Fluid Collections
                                    </div>

                                    <div class="col-lg-8">
                                        <div class="row">
                                            <div class="col-lg-3">
                                                    <a href="/docs/69345/Narrative/" target="_blank" class="download-pdf-icon2"></a>
<a class="wordwrap downloadLink" href="/docs/69345/Narrative/" target="_blank">Narrative &amp; Rating Table</a>                                            </div>
                                            <div class="col-lg-2">
                                                <a href="/docs/69345/EvidenceTable/" target="_blank" class="download-pdf-icon2"></a>
                                                <a class="wordwrap downloadLink" href="/list/GetEvidence?TopicId=9&amp;TopicName=Radiologic%20Management%20of%20Infected%20Fluid%20Collections" target="_blank">Evidence Table</a>
                                            </div>
                                            <div class="col-lg-2">
                                                    <a href="/list/ViewSearchStrategy?ReleaseId=103&amp;TopicId=9&amp;LitReviewID=116" target="_blank" class="download-pdf-icon2"></a>
                                                    <a href="/list/ViewSearchStrategy?ReleaseId=103&amp;TopicId=9&amp;LitReviewID=116" class="wordwrap downloadLink" target="_blank">Lit Search</a>
                                            </div>
                                            <div class="col-lg-2">
                                                <a href="/list/GenerateAppendixPDF?TopicId=9&amp;PanelName=Interventional Radiology" class="download-pdf-icon2" target="_blank" title="Click here to download"></a>
                                                <a href="/list/GetAppendix?TopicId=9&amp;PanelName=Interventional Radiology" title="Click here to download" target="_blank" class="wordwrap downloadLink">Appendix</a>
                                            </div>

                                            <div class="col-lg-3">
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="p-2 row divEven">
                                    <div class="col-lg-4">
Radiologic Management of Lower Gastrointestinal Tract Bleeding
                                    </div>

                                    <div class="col-lg-8">
                                        <div class="row">
                                            <div class="col-lg-3">
                                                    <a href="/docs/69457/Narrative/" target="_blank" class="download-pdf-icon2"></a>
<a class="wordwrap downloadLink" href="/docs/69457/Narrative/" target="_blank">Narrative &amp; Rating Table</a>                                            </div>
                                            <div class="col-lg-2">
                                                <a href="/docs/69457/EvidenceTable/" target="_blank" class="download-pdf-icon2"></a>
                                                <a class="wordwrap downloadLink" href="/list/GetEvidence?TopicId=115&amp;TopicName=Radiologic%20Management%20of%20Lower%20Gastrointestinal%20Tract%20Bleeding" target="_blank">Evidence Table</a>
                                            </div>
                                            <div class="col-lg-2">
                                                    <a href="/list/ViewSearchStrategy?ReleaseId=103&amp;TopicId=115&amp;LitReviewID=122" target="_blank" class="download-pdf-icon2"></a>
                                                    <a href="/list/ViewSearchStrategy?ReleaseId=103&amp;TopicId=115&amp;LitReviewID=122" class="wordwrap downloadLink" target="_blank">Lit Search</a>
                                            </div>
                                            <div class="col-lg-2">
                                                <a href="/list/GenerateAppendixPDF?TopicId=115&amp;PanelName=Interventional Radiology" class="download-pdf-icon2" target="_blank" title="Click here to download"></a>
                                                <a href="/list/GetAppendix?TopicId=115&amp;PanelName=Interventional Radiology" title="Click here to download" target="_blank" class="wordwrap downloadLink">Appendix</a>
                                            </div>

                                            <div class="col-lg-3">
                                                    <a href="https://www.jacr.org/article/S1546-1440(24)00921-9/pdf" class="link-icon downloadLink" target="_blank" title="Patient Summary">Patient Summary</a>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="p-2 row divOdd">
                                    <div class="col-lg-4">
Radiologic Management of Mesenteric Ischemia
                                    </div>

                                    <div class="col-lg-8">
                                        <div class="row">
                                            <div class="col-lg-3">
                                                    <a href="/docs/69501/Narrative/" target="_blank" class="download-pdf-icon2"></a>
<a class="wordwrap downloadLink" href="/docs/69501/Narrative/" target="_blank">Narrative &amp; Rating Table</a>                                            </div>
                                            <div class="col-lg-2">
                                                <a href="/docs/69501/EvidenceTable/" target="_blank" class="download-pdf-icon2"></a>
                                                <a class="wordwrap downloadLink" href="/list/GetEvidence?TopicId=159&amp;TopicName=Radiologic%20Management%20of%20Mesenteric%20Ischemia" target="_blank">Evidence Table</a>
                                            </div>
                                            <div class="col-lg-2">
                                                    <a href="/list/ViewSearchStrategy?ReleaseId=103&amp;TopicId=159&amp;LitReviewID=211" target="_blank" class="download-pdf-icon2"></a>
                                                    <a href="/list/ViewSearchStrategy?ReleaseId=103&amp;TopicId=159&amp;LitReviewID=211" class="wordwrap downloadLink" target="_blank">Lit Search</a>
                                            </div>
                                            <div class="col-lg-2">
                                                <a href="/list/GenerateAppendixPDF?TopicId=159&amp;PanelName=Interventional Radiology" class="download-pdf-icon2" target="_blank" title="Click here to download"></a>
                                                <a href="/list/GetAppendix?TopicId=159&amp;PanelName=Interventional Radiology" title="Click here to download" target="_blank" class="wordwrap downloadLink">Appendix</a>
                                            </div>

                                            <div class="col-lg-3">
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="p-2 row divEven">
                                    <div class="col-lg-4">
Radiologic Management of Portal Hypertension
                                    </div>

                                    <div class="col-lg-8">
                                        <div class="row">
                                            <div class="col-lg-3">
                                                    <a href="/docs/3102385/Narrative/" target="_blank" class="download-pdf-icon2"></a>
<a class="wordwrap downloadLink" href="/docs/3102385/Narrative/" target="_blank">Narrative &amp; Rating Table</a>                                            </div>
                                            <div class="col-lg-2">
                                                <a href="/docs/3102385/EvidenceTable/" target="_blank" class="download-pdf-icon2"></a>
                                                <a class="wordwrap downloadLink" href="/list/GetEvidence?TopicId=251&amp;TopicName=Radiologic%20Management%20of%20Portal%20Hypertension" target="_blank">Evidence Table</a>
                                            </div>
                                            <div class="col-lg-2">
                                                    <a href="/docs/3102385/LitSearch/" target="_blank" class="download-pdf-icon2"></a>
<a class="wordwrap downloadLink" href="/docs/3102385/LitSearch/" target="_blank">Lit Search</a>                                            </div>
                                            <div class="col-lg-2">
                                                <a href="/list/GenerateAppendixPDF?TopicId=251&amp;PanelName=Interventional Radiology" class="download-pdf-icon2" target="_blank" title="Click here to download"></a>
                                                <a href="/list/GetAppendix?TopicId=251&amp;PanelName=Interventional Radiology" title="Click here to download" target="_blank" class="wordwrap downloadLink">Appendix</a>
                                            </div>

                                            <div class="col-lg-3">
                                                    <a href="https://www.jacr.org/article/S1546-1440(24)00927-X/pdf" class="link-icon downloadLink" target="_blank" title="Patient Summary">Patient Summary</a>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="p-2 row divOdd">
                                    <div class="col-lg-4">
Radiologic Management of Pulmonary Nodules and Masses
                                    </div>

                                    <div class="col-lg-8">
                                        <div class="row">
                                            <div class="col-lg-3">
                                                    <a href="/docs/69343/Narrative/" target="_blank" class="download-pdf-icon2"></a>
<a class="wordwrap downloadLink" href="/docs/69343/Narrative/" target="_blank">Narrative &amp; Rating Table</a>                                            </div>
                                            <div class="col-lg-2">
                                                <a href="/docs/69343/EvidenceTable/" target="_blank" class="download-pdf-icon2"></a>
                                                <a class="wordwrap downloadLink" href="/list/GetEvidence?TopicId=7&amp;TopicName=Radiologic%20Management%20of%20Pulmonary%20Nodules%20and%20Masses" target="_blank">Evidence Table</a>
                                            </div>
                                            <div class="col-lg-2">
                                                    <a href="/docs/69343/LitSearch/" target="_blank" class="download-pdf-icon2"></a>
<a class="wordwrap downloadLink" href="/docs/69343/LitSearch/" target="_blank">Lit Search</a>                                            </div>
                                            <div class="col-lg-2">
                                                <a href="/list/GenerateAppendixPDF?TopicId=7&amp;PanelName=Interventional Radiology" class="download-pdf-icon2" target="_blank" title="Click here to download"></a>
                                                <a href="/list/GetAppendix?TopicId=7&amp;PanelName=Interventional Radiology" title="Click here to download" target="_blank" class="wordwrap downloadLink">Appendix</a>
                                            </div>

                                            <div class="col-lg-3">
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="p-2 row divEven">
                                    <div class="col-lg-4">
Radiologic Management of Urinary Tract Obstruction
                                    </div>

                                    <div class="col-lg-8">
                                        <div class="row">
                                            <div class="col-lg-3">
                                                    <a href="/docs/69353/Narrative/" target="_blank" class="download-pdf-icon2"></a>
<a class="wordwrap downloadLink" href="/docs/69353/Narrative/" target="_blank">Narrative &amp; Rating Table</a>                                            </div>
                                            <div class="col-lg-2">
                                                <a href="/docs/69353/EvidenceTable/" target="_blank" class="download-pdf-icon2"></a>
                                                <a class="wordwrap downloadLink" href="/list/GetEvidence?TopicId=17&amp;TopicName=Radiologic%20Management%20of%20Urinary%20Tract%20Obstruction" target="_blank">Evidence Table</a>
                                            </div>
                                            <div class="col-lg-2">
                                                    <a href="/list/ViewSearchStrategy?ReleaseId=103&amp;TopicId=17&amp;LitReviewID=36" target="_blank" class="download-pdf-icon2"></a>
                                                    <a href="/list/ViewSearchStrategy?ReleaseId=103&amp;TopicId=17&amp;LitReviewID=36" class="wordwrap downloadLink" target="_blank">Lit Search</a>
                                            </div>
                                            <div class="col-lg-2">
                                                <a href="/list/GenerateAppendixPDF?TopicId=17&amp;PanelName=Interventional Radiology" class="download-pdf-icon2" target="_blank" title="Click here to download"></a>
                                                <a href="/list/GetAppendix?TopicId=17&amp;PanelName=Interventional Radiology" title="Click here to download" target="_blank" class="wordwrap downloadLink">Appendix</a>
                                            </div>

                                            <div class="col-lg-3">
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="p-2 row divOdd">
                                    <div class="col-lg-4">
Radiologic Management of Venous Thromboembolism-Inferior Vena Cava Filters
                                    </div>

                                    <div class="col-lg-8">
                                        <div class="row">
                                            <div class="col-lg-3">
                                                    <a href="/docs/69342/Narrative/" target="_blank" class="download-pdf-icon2"></a>
<a class="wordwrap downloadLink" href="/docs/69342/Narrative/" target="_blank">Narrative &amp; Rating Table</a>                                            </div>
                                            <div class="col-lg-2">
                                                <a href="/docs/69342/EvidenceTable/" target="_blank" class="download-pdf-icon2"></a>
                                                <a class="wordwrap downloadLink" href="/list/GetEvidence?TopicId=6&amp;TopicName=Radiologic%20Management%20of%20Venous%20Thromboembolism-Inferior%20Vena%20Cava%20Filters" target="_blank">Evidence Table</a>
                                            </div>
                                            <div class="col-lg-2">
                                                    <a href="/docs/69342/LitSearch/" target="_blank" class="download-pdf-icon2"></a>
<a class="wordwrap downloadLink" href="/docs/69342/LitSearch/" target="_blank">Lit Search</a>                                            </div>
                                            <div class="col-lg-2">
                                                <a href="/list/GenerateAppendixPDF?TopicId=6&amp;PanelName=Interventional Radiology" class="download-pdf-icon2" target="_blank" title="Click here to download"></a>
                                                <a href="/list/GetAppendix?TopicId=6&amp;PanelName=Interventional Radiology" title="Click here to download" target="_blank" class="wordwrap downloadLink">Appendix</a>
                                            </div>

                                            <div class="col-lg-3">
                                                    <a href="https://www.jacr.org/article/S1546-1440(20)30409-9/pdf" class="link-icon downloadLink" target="_blank" title="Patient Summary">Patient Summary</a>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="p-2 row divEven">
                                    <div class="col-lg-4">
Thoracic Aortic Aneurysm or Dissection-Treatment Planning and Follow-Up
                                    </div>

                                    <div class="col-lg-8">
                                        <div class="row">
                                            <div class="col-lg-3">
                                                    <a href="/docs/3099659/Narrative/" target="_blank" class="download-pdf-icon2"></a>
<a class="wordwrap downloadLink" href="/docs/3099659/Narrative/" target="_blank">Narrative &amp; Rating Table</a>                                            </div>
                                            <div class="col-lg-2">
                                                <a href="/docs/3099659/EvidenceTable/" target="_blank" class="download-pdf-icon2"></a>
                                                <a class="wordwrap downloadLink" href="/list/GetEvidence?TopicId=237&amp;TopicName=Thoracic%20Aortic%20Aneurysm%20or%20Dissection-Treatment%20Planning%20and%20Follow-Up" target="_blank">Evidence Table</a>
                                            </div>
                                            <div class="col-lg-2">
                                                    <a href="/list/ViewSearchStrategy?ReleaseId=103&amp;TopicId=237&amp;LitReviewID=262" target="_blank" class="download-pdf-icon2"></a>
                                                    <a href="/list/ViewSearchStrategy?ReleaseId=103&amp;TopicId=237&amp;LitReviewID=262" class="wordwrap downloadLink" target="_blank">Lit Search</a>
                                            </div>
                                            <div class="col-lg-2">
                                                <a href="/list/GenerateAppendixPDF?TopicId=237&amp;PanelName=Interventional Radiology" class="download-pdf-icon2" target="_blank" title="Click here to download"></a>
                                                <a href="/list/GetAppendix?TopicId=237&amp;PanelName=Interventional Radiology" title="Click here to download" target="_blank" class="wordwrap downloadLink">Appendix</a>
                                            </div>

                                            <div class="col-lg-3">
                                                    <a href="https://www.jacr.org/article/S1546-1440(19)31031-2/pdf" class="link-icon downloadLink" target="_blank" title="Patient Summary">Patient Summary</a>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="p-2 row divOdd">
                                    <div class="col-lg-4">
Thoracoabdominal Aortic Aneurysm or Dissection: Treatment Planning and Follow-Up
                                    </div>

                                    <div class="col-lg-8">
                                        <div class="row">
                                            <div class="col-lg-3">
                                                    <a href="/docs/3185039/Narrative/" target="_blank" class="download-pdf-icon2"></a>
<a class="wordwrap downloadLink" href="/docs/3185039/Narrative/" target="_blank">Narrative &amp; Rating Table</a>                                            </div>
                                            <div class="col-lg-2">
                                                <a href="/docs/3185039/EvidenceTable/" target="_blank" class="download-pdf-icon2"></a>
                                                <a class="wordwrap downloadLink" href="/list/GetEvidence?TopicId=308&amp;TopicName=Thoracoabdominal%20Aortic%20Aneurysm%20or%20Dissection%3A%20Treatment%20Planning%20and%20Follow-Up" target="_blank">Evidence Table</a>
                                            </div>
                                            <div class="col-lg-2">
                                                    <a href="/list/ViewSearchStrategy?ReleaseId=103&amp;TopicId=308&amp;LitReviewID=201" target="_blank" class="download-pdf-icon2"></a>
                                                    <a href="/list/ViewSearchStrategy?ReleaseId=103&amp;TopicId=308&amp;LitReviewID=201" class="wordwrap downloadLink" target="_blank">Lit Search</a>
                                            </div>
                                            <div class="col-lg-2">
                                                <a href="/list/GenerateAppendixPDF?TopicId=308&amp;PanelName=Interventional Radiology" class="download-pdf-icon2" target="_blank" title="Click here to download"></a>
                                                <a href="/list/GetAppendix?TopicId=308&amp;PanelName=Interventional Radiology" title="Click here to download" target="_blank" class="wordwrap downloadLink">Appendix</a>
                                            </div>

                                            <div class="col-lg-3">
                                            </div>
                                        </div>
                                    </div>
                                </div>
            </div>

            
            
            

            

            

            
            
            
        </div>
    </div>
</div>

                            </div>
"""

# Base URL for relative links
base_url = "https://acsearch.acr.org"

# Directory to save PDFs
save_dir = "Narrative_PDFs"
os.makedirs(save_dir, exist_ok=True)

# Parse the HTML content
soup = BeautifulSoup(html_content, "html.parser")

# Find all "Narrative & Rating Table" links
narrative_links = soup.find_all("a", href=True, text=lambda x: x and "Narrative & Rating Table" in x)

# Download each PDF
for i, link in enumerate(narrative_links):
    relative_url = link['href']
    pdf_url = relative_url if relative_url.startswith("http") else f"{base_url}{relative_url}"
    pdf_name = f"{i}_Narrative.pdf"  # Name file based on the link structure
    pdf_path = os.path.join(save_dir, pdf_name)

    print(f"Downloading {pdf_name}...")
    try:
        response = requests.get(pdf_url)
        response.raise_for_status()  # Check for HTTP errors
        with open(pdf_path, "wb") as pdf_file:
            pdf_file.write(response.content)
        print(f"Saved {pdf_name} to {save_dir}")
    except Exception as e:
        print(f"Failed to download {pdf_name}: {e}")

print("Download complete.")