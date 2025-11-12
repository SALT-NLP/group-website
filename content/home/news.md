+++
# News section

widget = "blank"  # Use a blank widget for custom content
headless = true  # This file represents a page section.
active = true  # Activate this widget? true/false
weight = 2  # Order that this section will appear.

title = "Recent News"
subtitle = ""

[design]
  view = 2  # Choose your preferred layout

[design.background]
  # You can customize the background and text color if needed

[advanced]
 css_style = ""
 css_class = ""
+++


<style>
  .news-item {
    display: none;
  }
  .news-item:nth-child(-n+15) { /* Only display 15 latest news */
    display: table-row;
  }
  .no-hover-effect-or-stripes tr:hover td {
    background-color: inherit !important;
  }
  .no-hover-effect-or-stripes td {
    font-size: 1rem; /* Adjust to match <p> tags as needed */
  }
  .no-hover-effect-or-stripes > tbody > tr:nth-child(odd) > td,
  .no-hover-effect-or-stripes > tbody > tr:nth-child(odd) > th {
    background-color: inherit !important;
  }
</style>


<table class="no-hover-effect-or-stripes" style="border-collapse: collapse;">
  <tr class="news-item">
    <td style="border: none;">11/2025</td>
    <td style="border: none;">Our two spotlight papers have been accepted to <a href="https://neurips.cc/Conferences/2025">NeurIPS 2025</a>!</td>
  </tr>
  <tr class="news-item">
    <td style="border: none;">05/2025</td>
    <td style="border: none;">SALT lab has seven papers accepted to <a href="https://2025.aclweb.org/">ACL 2025</a> Main/Findings and <a href="https://icml.cc/Conferences/2025">ICML 2025</a>!</td>
  </tr>
  <tr class="news-item">
    <td style="border: none;">01/2025</td>
    <td style="border: none;">SALT lab has two papers on AI for frontend developing accepted to <a href="https://2025.naacl.org/">NAACL 2025</a> and four papers accepted to <a href="https://iclr.cc/">ICLR 2025</a>!</td>
  </tr>
  <tr class="news-item">
    <td style="border: none;">09/2024</td>
    <td style="border: none;">SALT lab has seven papers accepted to <a href="https://2024.emnlp.org/">EMNLP 2024</a> (three to the main conference and four to the findings). We also have two papers accepted to <a href="https://dl.acm.org/conference/cscw">CSCW</a>. Congrats on these amazing efforts!</td>
  </tr>
  <tr class="news-item">
    <td style="border: none;">08/2024</td>
    <td style="border: none;">Diyi gave an invited talk at <a href="https://summit.newturing.ai/">GenAI summit</a> in Vietnam.</td>
  </tr>
  <tr class="news-item">
    <td style="border: none;">08/2024</td>
    <td style="border: none;">Our group's research on aligning AI chatbots is covered by Stanford HAI. <a href="https://hai.stanford.edu/news/challenge-aligning-ai-chatbots">Read the coverage!</a></td>
  </tr>
  <tr class="news-item">
    <td style="border: none;">07/2024</td>
    <td style="border: none;"><a href="https://arxiv.org/abs/2310.02170">Dynamic LLM-Agent Network</a> is accepted to the first COLM. Congratulations to Zijun and Yanzhe!</td>
  </tr>
  <tr class="news-item">
    <td style="border: none;">05/2024</td>
    <td style="border: none;">SALT Lab has seven papers accepted to <a href="https://2024.aclweb.org/">ACL 2024</a>, three to the main conference and four to the findings. See you in Bangkok!</td>
  </tr>
  <tr class="news-item">
    <td style="border: none;">03/2024</td>
    <td style="border: none;">Omar's paper "Grounding or Guesswork? Large Language Models are Presumptive Grounders" is accepted to NAACL main conference. Check out the <a href="https://arxiv.org/abs/2311.09144">preprint</a>.</td>
  </tr>
  <tr class="news-item">
    <td style="border: none;">02/2024</td>
    <td style="border: none;">Diyi received <a href="https://sloan.org/fellowships/2024-Fellows">2024 Sloan Research Fellowships</a>.</td>
  </tr>
  <tr class="news-item">
    <td style="border: none;">02/2024</td>
    <td style="border: none;">Diyi received <a href="https://www.nre.navy.mil/2024-young-investigators">ONR Young Investigator Award</a>.</td>
  </tr>
  <tr class="news-item">
    <td style="border: none;">11/2023</td>
    <td style="border: none;">Jiaao passed his thesis proposal!</td>
  </tr>
  <tr class="news-item">
    <td style="border: none;">10/2023</td>
    <td style="border: none;">Camille's <a href="https://dl.acm.org/doi/10.1145/3610169">CSCW 2023 paper</a> has been awarded Recognition for Contribution to Diversity and Inclusion!</td>
  </tr>
</table>