from bs4 import BeautifulSoup
import os

html_content = """  <div id="main">
<h2>Recent Preprints</h2>
<ul>
	<li class="paper_wrapper_selected">
        <p class="paper_title">Helping the Helper: Supporting Peer Counselors via AI-Empowered Practice and Feedback</p>
        <p class="paper_authors">Shang-Ling Hsu, Raj Sanjay Shah, Prathik Senthil, Zahra Ashktorab, Casey Dugan, Werner Geyer, Diyi Yang</p>
        <p class="paper_venue"> arXiv:2305.08982. <a href="https://arxiv.org/abs/2305.08982"><u>[pdf]</u></a></p>
      	</li>
	<li class="paper_wrapper_selected">
	<p class="paper_title">LLaVAR: Enhanced Visual Instruction Tuning for Text-Rich Image Understanding</p>
	<p class="paper_authors">Yanzhe Zhang, Ruiyi Zhang, Jiuxiang Gu, Yufan Zhou, Nedim Lipka, Diyi Yang, Tong Sun</p>
	<p class="paper_venue">arXiv:2306.17107, 2023. <a href="https://arxiv.org/abs/2306.17107">[pdf]</a></p>
	</li>
	<li class="paper_wrapper_selected">
	<p class="paper_title">Dynamic LLM-Agent Network: An LLM-agent Collaboration Framework with Agent Team Optimization</p>
	<p class="paper_authors">Zijun Liu, Yanzhe Zhang, Peng Li, Yang Liu, Diyi Yang</p>
	<p class="paper_venue">arXiv:2310.02170 , 2023. <a href="https://arxiv.org/abs/2310.02170">[pdf]</a></p>
	</li>
</ul>

<h2>Publications <a href="https://scholar.google.com/citations?user=j9jhYqQAAAAJ&amp;hl=en"><small>[Google Scholar]</small></a>
      <button class="button-4" role="button" id="btn_selected" autofocus><small>[Show Selected]</small></button>
      <button class="button-4" role="button" id="btn_all"><small>[Show All]</small></button>
  </h2>

    <!-- <button id="btn_all">Show All</button> -->
    <script src="index.js"></script>
<ul>
<li class="paper_wrapper_selected">
        <p class="paper_title">Rehearsal: Simulating Conflict to Teach Conflict Resolution</p>
        <p class="paper_authors">Omar Shaikh, Valentino Chai, Michele J. Gelfand, Diyi Yang, Michael S. Bernstein</p>
        <p class="paper_venue"> CHI, 2024 . <a href="https://arxiv.org/abs/2309.12309"><u>[pdf]</u></a></p>
        </li>
 <li class="paper_wrapper_selected">
        <p class="paper_title">DyVal: Graph-informed Dynamic Evaluation of Large Language Models</p>
        <p class="paper_authors">Kaijie Zhu, Jiaao Chen, Jindong Wang, Neil Zhenqiang Gong, Diyi Yang, Xing Xie</p>
        <p class="paper_venue"> ICLR, 2024. <a href="https://arxiv.org/abs/2309.17167">[pdf]</a></p>
        </li>
<li class="paper_wrapper_selected">
<p class="paper_title">Using Large Language Models in Psychology</p>
<p class="paper_authors">Dorottya Demszky*, Diyi Yang*, David S. Yeager*, Christopher J. Bryan, Margarett Clapper, Susannah Chandhok, Johannes C. Eichstaedt, Cameron Hecht, Jeremy Jamieson, Meghann Johnson, Michaela Jones, Danielle Krettek-Cobb, Leslie Lai, Nirel JonesMitchell, Desmond C. Ong, Carol S. Dweck, James J. Gross, James W. Pennebaker </p>
<p class="paper_venue">Nature Reviews Psychology, 2023. <a href="https://www.nature.com/articles/s44159-023-00241-5">[pdf]</a></p>
</li>
 <li class="paper_wrapper_selected">
        <p class="paper_title">Can Large Language Models Transform Computational Social Science?</p>
        <p class="paper_authors">Caleb Ziems, William Held, Omar Shaikh, Jiaao Chen, Zhehao Zhang, Diyi Yang</p>
        <p class="paper_venue">Computational Linguistics, 2023. <a href="https://arxiv.org/abs/2305.03514"><u>[pdf]</u></a></p>
        </li>
<li class="paper_wrapper_selected">
<p class="paper_title">Unlearn What You Want to Forget: Efficient Unlearning for LLMs</p>
<p class="paper_authors">Jiaao Chen, Diyi Yang</p>
<p class="paper_venue">EMNLP, 2023. <a href="https://arxiv.org/abs/2310.20150">[pdf]</a></p>
</li>
<li class="paper_wrapper_selected">
<p class="paper_title">CoMPosT: Characterizing and Evaluating Caricature in LLM Simulations</p>
<p class="paper_authors">Myra Cheng, Tiziano Piccardi, Diyi Yang</p>
<p class="paper_venue">EMNLP, 2023. <a href="https://arxiv.org/abs/2310.11501">[pdf]</a></p>
</li>
<li class="paper_wrapper_selected">
<p class="paper_title">DADA: Dialect Adaptation via Dynamic Aggregation of Linguistic Rules</p>
<p class="paper_authors">Yanchen Liu, William Held, Diyi Yang</p>
<p class="paper_venue">EMNLP, 2023. <a href="https://arxiv.org/abs/2305.13406">[pdf]</a></p>
</li>
<li class="paper_wrapper_all">
<p class="paper_title">Is ChatGPT a General-Purpose Natural Language Processing Task Solver?</p>
<p class="paper_authors">Chengwei Qin, Aston Zhang, Zhuosheng Zhang, Jiaao Chen, Michihiro Yasunaga, Diyi Yang</p>
<p class="paper_venue">EMNLP, 2023. <a href="https://arxiv.org/abs/2302.06476">[pdf]</a></p>
</li>
<li class="paper_wrapper_selected">
<p class="paper_title">CoAnnotating: Uncertainty-Guided Work Allocation between Human and Large Language Models for Data Annotation</p>
<p class="paper_authors">Ella Li, Taiwei Shi, Caleb Ziems, Min-Yen Kan, Nancy F. Chen, Zhengyuan Liu, Diyi Yang</p>
<p class="paper_venue">EMNLP, 2023. <a href="https://arxiv.org/abs/2310.15638">[pdf]</a></p>
</li>
<li class="paper_wrapper_selected">
<p class="paper_title">Impressions: Visual Semiotics and Aesthetic Impact Understanding</p>
<p class="paper_authors">Julia Kruk, Caleb Ziems, Diyi Yang</p>
<p class="paper_venue">EMNLP, 2023. <a href="https://arxiv.org/abs/2310.17887">[pdf]</a></p>
</li>
<li class="paper_wrapper_all">
<p class="paper_title">Generating and Evaluating Tests for K-12 Students with Language Model Simulations: A Case Study on Sentence Reading Efficiency</p>
<p class="paper_authors">Eric Zelikman, Wanjing Anya Ma, Jasmine Elizabeth Tran, Diyi Yang, Jason D Yeatman, Nick Haber</p>
<p class="paper_venue">EMNLP, 2023. <a href="https://arxiv.org/abs/2310.06837">[pdf]</a></p>
</li>
	<li class="paper_wrapper_selected">
        <p class="paper_title">Understanding Black Content Creator Experiences on TikTok</p>
        <p class="paper_authors">Camille Harris, Amber Gayle Johnson, Sadie Palmer, Diyi Yang, Amy Bruckman</p>
	<p class="paper_venue">CSCW, 2023. <a href="https://dl.acm.org/doi/abs/10.1145/3610169">[pdf]</a></p>
	<p class="paper_note">Recognition for Contribution to Diversity and Inclusion Award</p>
        </li>
	<li class="paper_wrapper_selected">
        <p class="paper_title">Multi-VALUE: A Framework for Cross-Dialectal English NLP</p>
        <p class="paper_authors">Caleb Ziems, William Held, Jingfeng Yang, Jwala Dhamala, Rahul Gupta, Diyi Yang</p>
        <p class="paper_venue"> ACL, 2023. <a href="https://arxiv.org/abs/2212.08011"><u>[pdf]</u></a><a href="https://value-nlp.org/">[website]</a></p>
      	</li>
	<li class="paper_wrapper_selected">
        <p class="paper_title">NormBank: A Knowledge Bank of Situational Social Norms</p>
        <p class="paper_authors">Caleb Ziems, Jane Dwivedi-Yu, Yi-Chia Wang, Alon Halevy, Diyi Yang</p>
        <p class="paper_venue"> ACL, 2023. <a href="https://arxiv.org/abs/2305.17008"><u>[pdf]</u></a></p>
      	</li>
	<li class="paper_wrapper_selected">
        <p class="paper_title">On Second Thought, Let's Not Think Step by Step! Bias and Toxicity in Zero-Shot Reasoning</p>
        <p class="paper_authors">Omar Shaikh, Hongxin Zhang, William Held, Michael S. Bernstein, Diyi Yang</p>
        <p class="paper_venue"> ACL, 2023. <a href="https://arxiv.org/abs/2212.08061"><u>[pdf]</u></a></p>
        </li>
	<li class="paper_wrapper_selected">
        <p class="paper_title">Forgotten Knowledge: Examining the Citational Amnesia in NLP</p>
        <p class="paper_authors">Janvijay Singh, Mukund Rungta, Diyi Yang, Saif M. Mohammad</p>
        <p class="paper_venue"> ACL, 2023. <a href="https://arxiv.org/abs/2305.18554"><u>[pdf]</u></a></p>
        <p class="paper_note">Best Paper Honorable Mention</p>
	</li>
	<li class="paper_wrapper_selected">
        <p class="paper_title">Human-in-the-loop Abstractive Dialogue Summarization</p>
        <p class="paper_authors">Jiaao Chen, Mohan Dodda, Diyi Yang</p>
        <p class="paper_venue"> ACL (Findings), 2023. <a href="https://arxiv.org/abs/2212.09750"><u>[pdf]</u></a></p>
        </li>
	<li class="paper_wrapper_selected">
        <p class="paper_title">Task Agnostic Dialect Adapters for English</p>
        <p class="paper_authors">William Held, Caleb Ziems, Diyi Yang</p>
        <p class="paper_venue"> ACL (Findings), 2023. <a href="https://arxiv.org/abs/2305.16651"><u>[pdf]</u></a></p>
        </li>
	<li class="paper_wrapper_selected">
        <p class="paper_title">Modeling Cross-Cultural Pragmatic Inference with Codenames Duet</p>
        <p class="paper_authors">Omar Shaikh, Caleb Ziems, William Held, Aryan J. Pariani, Fred Morstatter, Diyi Yang</p>
        <p class="paper_venue"> ACL (Findings), 2023. <a href="https://arxiv.org/abs/2306.02475"><u>[pdf]</u></a></p>
        </li>
        <li class="paper_wrapper_selected">
        <p class="paper_title">Parameter-Efficient Fine-Tuning Design Spaces</p>
        <p class="paper_authors">Jiaao Chen, Aston Zhang, Xingjian Shi, Mu Li, Alex Smola, Diyi Yang</p>
        <p class="paper_venue"> ICLR, 2023. <a href="https://arxiv.org/abs/2301.01821"><u>[pdf]</u></a></p>
      	</li>
 	<li class="paper_wrapper_selected">
        <p class="paper_title">Shapley Head Pruning: Identifying and Removing Interference in Multilingual Transformers</p>
        <p class="paper_authors">William Held, Diyi Yang</p>
        <p class="paper_venue"> EACL, 2023. <a href="https://arxiv.org/abs/2210.05709"><u>[pdf]</u></a></p>
      </li>
	<li class="paper_wrapper_all">
        <p class="paper_title">Bounding the Capabilities of Large Language Models in Open Text Generation with Prompt Constraints</p>
        <p class="paper_authors">Albert Lu, Hongxin Zhang, Yanzhe Zhang, Xuezhi Wang, Diyi Yang</p>
        <p class="paper_venue"> EACL (Findings), 2023. <a href="https://arxiv.org/abs/2302.09185"><u>[pdf]</u></a></p>
      </li>
<li class="paper_wrapper_all">
        <p class="paper_title">Metrics for Peer Counseling: Triangulating Success Outcomes for Online Therapy Platforms</p>
        <p class="paper_authors">Tony Wang, Haard K Shah, Raj Sanjay Shah, Yi-Chia Wang, Robert Kraut, Diyi Yang</p>
        <p class="paper_venue"> SIGCHI, 2023. <a href="./docs/chi2023_wang.pdf"><u>[pdf]</u></a></p>
      </li>

<li class="paper_wrapper_all">
	<p class="paper_title">An Empirical Survey of Data Augmentation for Limited Data Learning in NLP</p>
        <p class="paper_authors">Jiaao Chen, Derek Tam, Colin Raffel, Mohit Bansal, Diyi Yang</p>
        <p class="paper_venue">TACL. <a href="https://arxiv.org/abs/2106.07499"><u>[pdf]</u></a></p>
      </li>
<li class="paper_wrapper_all">
	<p class="paper_title">Causal Inference in Natural Language Processing: Estimation, Prediction, Interpretation and Beyond</p>
        <p class="paper_authors">Amir Feder, Katherine A Keith, Emaad Manzoor, Reid Pryzant, Dhanya Sridhar, Zach Wood-Doughty, Jacob Eisenstein, Justin Grimmer, Roi Reichart, Margaret E Roberts, Brandon M Stewart, Victor Veitch, Diyi Yang</p>
        <p class="paper_venue">TACL. <a href="https://arxiv.org/abs/2109.00725"><u>[pdf]</u></a></p>
	</li>
<li class="paper_wrapper_selected">
	<p class="paper_title">Geographic Citation Gaps in NLP Research</p>
	<p class="paper_authors">Mukund Rungta, Janvijay Singh, Saif M. Mohammad, Diyi Yang</p>
	<p class="paper_venue">EMNLP, 2022. <a href="https://arxiv.org/abs/2210.14424"><u>[pdf]</u></a></p>
        </li>
<li class="paper_wrapper_all">
	<p class="paper_title">When FLUE Meets FLANG: Benchmarks and Large Pretrained Language Model for Financial Domain</p>
        <p class="paper_authors">Raj Sanjay Shah, Kunal Chawla, Dheeraj Eidnani, Agam Shah, Wendi Du, Sudheer Chava, Natraj Raman, Charese Smiley, Jiaao Chen, Diyi Yang</p>
        <p class="paper_venue">EMNLP, 2022. <a href="./docs/emnlp_flang_2022.pdf"><u>[pdf]</u></a></p>
        </li>
<li class="paper_wrapper_selected">
	<p class="paper_title">Robustness of Demonstration-based Learning Under Limited Data Scenario</p>
        <p class="paper_authors">Hongxin Zhang, Yanzhe Zhang, Ruiyi Zhang, Diyi Yang</p>
        <p class="paper_venue">EMNLP, 2022. <a href="https://arxiv.org/abs/2210.10693"><u>[pdf]</u></a></p>
	</li>
<li class="paper_wrapper_all">
        <p class="paper_title">A Sketch Is Worth a Thousand Words: Image Retrieval with Text and Sketch</p>
        <p class="paper_authors">Patsorn Sangkloy, Wittawat Jitkrittum, Diyi Yang, James Hays</p>
        <p class="paper_venue">ECCV, 2022. <a href="https://arxiv.org/abs/2208.03354"><u>[pdf]</u></a></p>
        </li>
<li class="paper_wrapper_selected">
	<p class="paper_title">Modeling Motivational Interviewing Strategies On Online Peer-to-Peer Counseling Platforms</p>
	<p class="paper_authors">Raj Sanjay Shah, Faye Holt, Shirley Anugrah Hayati, Aastha Agrawal, Yi-Chia Wang, Robert Kraut, Diyi Yang</p>
	<p class="paper_venue">CSCW, 2022. <a href="./docs/cscw2022_miti.pdf"><u>[pdf]</u></a></p>
	</li>
<li class="paper_wrapper_all">
        <p class="paper_title">SUBS: Subtree Substitution for Compositional Semantic Parsing</p>
        <p class="paper_authors">Jingfeng Yang, Le Zhang, Diyi Yang</p>
        <p class="paper_venue">NAACL, 2022. <a href="https://arxiv.org/abs/2205.01538"><u>[pdf]</u></a></p>
      </li>
<li class="paper_wrapper_selected">
        <p class="paper_title">TreeMix: Compositional Constituency-based Data Augmentation for Natural Language Understanding</p>
        <p class="paper_authors">Le Zhang, Zichao Yang, Diyi Yang</p>
        <p class="paper_venue">NAACL, 2022. <a href="./docs/naacl_treemix.pdf"><u>[pdf]</u></a></p>
      </li>
<li class="paper_wrapper_all">
        <p class="paper_title">Explaining Toxic Text via Knowledge Enhanced Text Generation</p>
        <p class="paper_authors">Rohit Sridhar, Diyi Yang</p>
        <p class="paper_venue">NAACL, 2022. <a href="./docs/naacl_exp.pdf"><u>[pdf]</u></a></p>
      </li>
<li class="paper_wrapper_all">
        <p class="paper_title">Measure and Improve Robustness in NLP Models: A Survey</p>
        <p class="paper_authors">Xuezhi Wang, Haohan Wang, Diyi Yang</p>
        <p class="paper_venue">NAACL, 2022. <a href="https://arxiv.org/abs/2112.08313"><u>[pdf]</u></a></p>
      </li>
<li class="paper_wrapper_all">
        <p class="paper_title">Identifying and Mitigating Spurious Correlations for Improving Robustness in NLP Models</p>
        <p class="paper_authors">Tianlu Wang, Rohit Sridhar, Diyi Yang, Xuezhi Wang</p>
        <p class="paper_venue">NAACL (Findings), 2022. <a href="https://arxiv.org/abs/2110.07736"><u>[pdf]</u></a></p>
      </li>
<li class="paper_wrapper_all">
        <p class="paper_title">Few-shot Compositional Semantic Parsing with Sequential Prompts and Zero-shot Models</p>
        <p class="paper_authors">Jingfeng Yang, Haoming Jiang, Qingyu Yin, Danqing Zhang, Bing Yin, Diyi Yang</p>
        <p class="paper_venue">NAACL (Findings), 2022. <a href="./docs/naacl_seqzero.pdf"><u>[pdf]</u></a></p>
      </li>
<li class="paper_wrapper_all">
        <p class="paper_title">Exploring the Role of Grammar and Word Choice in Bias Toward AAVE in Hate Speech Classification</p>
        <p class="paper_authors">Camille Harris, Matan Halevy, Ayanna Howard, Amy Bruckman, Diyi Yang</p>
        <p class="paper_venue">FAccT, 2022. <a href=""><u>[pdf]</u></a></p>
      </li>
<li class="paper_wrapper_selected">
        <p class="paper_title">VALUE: Understanding Dialect Disparity in NLU</p>
        <p class="paper_authors">Caleb Ziems, Jiaao Chen, Camille Harris, Jessica Anderson, Diyi Yang</p>
        <p class="paper_venue">ACL, 2022. <a href="https://arxiv.org/abs/2204.03031"><u>[pdf]</u></a> <a href="https://drive.google.com/file/d/1OrRYmG1IFX5cqVQCGyZ1mboa7dCyA3IW/view?usp=sharing"><u>[slides]</u></a></p>
      </li>
<li class="paper_wrapper_selected">
        <p class="paper_title">Inducing Positive Perspectives with Text Reframing</p>
        <p class="paper_authors">Caleb Ziems, Minzhi Li, Anthony Zhang, Diyi Yang</p>
        <p class="paper_venue">ACL, 2022. <a href="https://arxiv.org/abs/2204.02952"><u>[pdf]</u></a></p>
	<p class="paper_note">Outstanding Paper Award</p>      
</li>
<li class="paper_wrapper_selected">
        <p class="paper_title">Continual Sequence Generation with Adaptive Compositional Modules</p>
        <p class="paper_authors">Yanzhe Zhang, Xuezhi Wang, Diyi Yang</p>
        <p class="paper_venue">ACL, 2022. <a href="https://arxiv.org/abs/2203.10652"><u>[pdf]</u></a></p>
      </li>
<li class="paper_wrapper_all">
        <p class="paper_title">Moral Integrity Corpus: A Benchmark for Ethical Dialogue Systems</p>
        <p class="paper_authors">Caleb Ziems, Jane A. Yu, Yi-Chia Wang, Alon Halevy, Diyi Yang</p>
        <p class="paper_venue">ACL, 2022. <a href="https://arxiv.org/abs/2204.03021"><u>[pdf]</u></a></p>
      </li>

<li class="paper_wrapper_all">
        <p class="paper_title">Focus on the Action: Learning to Highlight and Summarize Jointly for Email To-Do Items Summarization</p>
        <p class="paper_authors">Kexun Zhang, Jiaao Chen, Diyi Yang</p>
        <p class="paper_venue">ACL (Findings), 2022. <a href="./docs/acl22_summarization.pdf"><u>[pdf]</u></a></p>
      </li>
<li class="paper_wrapper_all">
        <p class="paper_title">FairytaleQA: An Authentic Dataset for Narrative Comprehension</p>
        <p class="paper_authors">Ying Xu, Dakuo Wang, Mo Yu, Daniel Ritchie, Bingsheng Yao, Tongshuang Wu, Zheng Zhang, Toby Jia-Jun Li, Nora Bradford, Branda Sun, Tran Bao Hoang, Yisi Sang, Yufang Hou, Xiaojuan Ma, Diyi Yang, Nanyun Peng, Zhou Yu, Mark Warschauer</p>
        <p class="paper_venue">ACL, 2022. <a href="https://arxiv.org/abs/2203.13947"><u>[pdf]</u></a></p>
      </li>
<li class="paper_wrapper_selected">
	<p class="paper_title"> GNN is a Counter? Revisiting GNN for Question Answering</p>
	<p class="paper_authors">Kuan Wang, Yuyu Zhang, Diyi Yang, Le Song, Tao Qin</p>
  	<p class="paper_venue">ICLR, 2022. <a href="https://arxiv.org/abs/2110.03192"><u>[pdf]</u></a></p>
      </li>
<li class="paper_wrapper_selected">
        <p class="paper_title">Will AI Console Me when I Lose my Pet? Understanding Perceptions of AI-Mediated Email Writing</p>
        <p class="paper_authors">Yihe Liu, Anushk Mittal, Diyi Yang, Amy Bruckman</p>
        <p class="paper_venue">CHI, 2022. <a href="./docs/chi22_perception.pdf"><u>[pdf]</u></a></p>
      </li>
<li class="paper_wrapper_selected">
        <p class="paper_title">Pretty Princess vs. Successful Leader: Gender Roles in Greeting Card Messages</p>
        <p class="paper_authors">Jiao Sun, Tongshuang Wu, Yue Jiang, Ronil Awalegaonkar, Xi Victoria Lin and Diyi Yang</p>
        <p class="paper_venue">CHI, 2022. <a href="https://arxiv.org/abs/2112.13980"><u>[pdf]</u></a></p>
	<p class="paper_note">Best Paper Honorable Mention</p>
      </li>
<li class="paper_wrapper_all">
<p class="paper_title">Linguistic Characterization of Divisive Topics Online: Case Studies on Contentiousness in Abortion, Climate Change, and Gun Control</p>
<p class="paper_authors">Jacob Beel, Tong Xiang, Sandeep Soni, Diyi Yang</p>
  <p class="paper_venue">ICWSM 2022. <a href="https://arxiv.org/abs/2108.13556"><u>[pdf]</u></a></p>
      </li>
<li class="paper_wrapper_selected">
        <p class="paper_title">
Simple Conversational Data Augmentation for Semi-supervised Abstractive Dialogue Summarization</p>
        <p class="paper_authors">Jiaao Chen, Diyi Yang</p>
        <p class="paper_venue">EMNLP, 2021. <a href="./docs/emnlp21_chen_coda.pdf"><u>[pdf]</u></a></p>
      </li>
<li class="paper_wrapper_selected">
        <p class="paper_title">
Latent Hatred: A Benchmark for Understanding Implicit Hate Speech</p>
        <p class="paper_authors">Mai ElSherief*, Caleb Ziems*, David Muchlinski, Vaishnavi Anupindi, Jordyn Seybolt, Munmun De Choudhury, Diyi Yang</p>
        <p class="paper_venue">EMNLP, 2021. <a href="https://arxiv.org/pdf/2109.05322.pdf"><u>[pdf]</u></a></p>
      </li>
<li class="paper_wrapper_selected">
        <p class="paper_title">To Protect and To Serve? Analyzing Entity-Centric Framing of Police Violence</p>
        <p class="paper_authors">Caleb Ziems, Diyi Yang</p>
        <p class="paper_venue">EMNLP (Findings), 2021. <a href="https://arxiv.org/pdf/2109.05325.pdf"><u>[pdf]</u></a></p>
      </li>
 <li class="paper_wrapper_selected">
        <p class="paper_title">RECAST: Enabling User Recourse and Interpretability of Toxicity Detection Models with Interactive Visualization</p>
        <p class="paper_authors">Austin P Wright, Omar Shaikh, Haekyu Park, Will Epperson, Muhammed Ahmed, Stephane Pinel, Duen Horng (Polo) Chau, Diyi Yang</p>
        <p class="paper_venue">CSCW, 2021. <a href="https://arxiv.org/abs/2102.04427"><u>[pdf]</u></a></p>
      </li>
<li class="paper_wrapper_selected">
        <p class="paper_title">Evaluating the Effectiveness of Deplatforming as a Moderation Strategy on Twitter</p>
        <p class="paper_authors">Shagun Jhaver, Christian Boylston, Diyi Yang, Amy Bruckman</p>
        <p class="paper_venue">CSCW, 2021. <a href="./docs/jhaver-2021-deplatforming.pdf"><u>[pdf]</u></a></p>
       <p class="paper_note">Best Paper Honorable Mention</p>
	</li>
<li class="paper_wrapper_all">
        <p class="paper_title">Mitigating Racial Biases in Toxic Language Detection with an Equity-Based Ensemble Framework</p>
        <p class="paper_authors">Matan Halevy, Camille Harris, Amy Bruckman, Diyi Yang, Ayanna Howard</p>
        <p class="paper_venue">ACM conference on Equity and Access in Algorithms, Mechanisms, and Optimization (EAAMO), 2021. <a href="https://arxiv.org/abs/2109.13137"><u>[pdf]</u></a></p>
	<p class="paper_note">Best Student Paper Award</p>
      </li>
<li class="paper_wrapper_selected">
        <p class="paper_title">Understanding the Usage of Online Media for Parenting from Infancy to Preschool At Scale</p>
        <p class="paper_authors">Yujia Gao, Jinu Jang, Diyi Yang</p>
        <p class="paper_venue">SIGCHI, 2021. <a href="./docs/chi21_gao.pdf"><u>[pdf]</u></a></p>
        <p class="paper_note">Best Paper Honorable Mention</p>
      </li>
<li class="paper_wrapper_all">
        <p class="paper_title">HiddenCut: Simple Data Augmentation for Natural Language Understanding with Better Generalizability</p>
        <p class="paper_authors">Jiaao Chen, Dinghan Shen, Weizhu Chen, Diyi Yang</p>
        <p class="paper_venue">ACL, 2021. <a href="./docs/acl21_hiddencut.pdf"><u>[pdf]</u></a></p>
      </li>
    <li class="paper_wrapper_all">
        <p class="paper_title">A Dataset for Understanding Disfluencies in Question Answering</p>
        <p class="paper_authors">Aditya Gupta, Jiacheng Xu, Shyam Upadhyay, Diyi Yang, Manaal Faruqui</p>
        <p class="paper_venue">ACL (Findings), 2021. <a href="./docs/acl21_disfluency.pdf"><u>[pdf]</u></a></p>
      </li>
    <li class="paper_wrapper_selected">
        <p class="paper_title">Structure-Aware Abstractive Conversation Summarization via Discourse and Action Graphs</p>
        <p class="paper_authors">Jiaao Chen, Diyi Yang</p>
        <p class="paper_venue">NAACL, 2021. <a href="./docs/naacl21_chen_summarization.pdf"><u>[pdf]</u></a></p>
      </li>
    <li class="paper_wrapper_selected">
        <p class="paper_title">Continual Learning for Text Classification with Information Disentanglement Based Regularization</p>
        <p class="paper_authors">Yufan Huang, Yanzhe Zhang, Jiaao Chen, Xuezhi Wang and Diyi Yang</p>
        <p class="paper_venue">NAACL, 2021. <a href="./docs/naacl21_cl.pdf"><u>[pdf]</u></a></p>
      </li>
      <li class="paper_wrapper_all">
        <p class="paper_title">Personalized Response Generation via Generative Split Memory Network</p>
        <p class="paper_authors">Yuwei Wu, Xuezhe Ma,Diyi Yang</p>
        <p class="paper_venue">NAACL, 2021. <a href="./docs/naacl21_personalization.pdf"><u>[pdf]</u></a></p>
      </li>
     <li class="paper_wrapper_selected">
        <p class="paper_title">The Importance of Modeling Social Factors of Language: Theory and Practice</p>
        <p class="paper_authors">Dirk Hovy, Diyi Yang</p>
        <p class="paper_venue">NAACL, 2021. <a href="./docs/naacl21_social.pdf"><u>[pdf]</u></a></p>
      </li>
      <li class="paper_wrapper_all">
        <p class="paper_title">Weakly-Supervised Hierarchical Models for Predicting Persuasive Strategies in Good-faith Textual Requests</p>
        <p class="paper_authors">Jiaao Chen, Diyi Yang</p>
        <p class="paper_venue">AAAI, 2021. <a href="./docs/aaai21_chen.pdf"><u>[pdf]</u></a></p>
      </li>
      <li class="paper_wrapper_all">
        <p class="paper_title">Tuiteamos o pongamos un tuit? Investigating the Social Constraints of Loanword Integration in Spanish Social Media</p>
        <p class="paper_authors">Ian Stewart, Diyi Yang, Jacob Eisenstein</p>
        <p class="paper_venue">The Society for Computation in Linguistics (SCiL), 2021. <a href="./docs/scil21_stewart.pdf"><u>[pdf]</u></a></p>
      </li>
    <li class="paper_wrapper_selected">
        <p class="paper_title">Multi-View Sequence-to-Sequence Models with Conversational Structure for Abstractive Dialogue Summarization</p>
        <p class="paper_authors">Jiaao Chen, Diyi Yang</p>
        <p class="paper_venue">EMNLP, 2020. <a href="https://arxiv.org/abs/2010.01672"><u>[pdf]</u></a> <a href="https://www.cc.gatech.edu/news/641381/need-note-taker-ai-can-help"><u>[news]</u></a></p>
      </li>
    <li class="paper_wrapper_all">
        <p class="paper_title">Local Additivity Based Data Augmentation for Semi-supervised NER</p>
        <p class="paper_authors">Jiaao Chen*, Zhenghui Wang*, Ran Tian, Zichao Yang and Diyi Yang</p>
        <p class="paper_venue">EMNLP, 2020. <a href="https://arxiv.org/abs/2010.01677"><u>[pdf]</u></a></p>
      </li>
      <li class="paper_wrapper_all">
        <p class="paper_title">Planning and Generating Natural and Diverse Disfluent Texts as Augmentation for Disfluency Detection</p>
        <p class="paper_authors">Jingfeng Yang, Zhaoran Ma, and Diyi Yang</p>
        <p class="paper_venue">EMNLP, 2020. <a href="./docs/emnlp20_disfluency.pdf"><u>[pdf]</u></a></p>
      </li>
    <li class="paper_wrapper_all">
        <p class="paper_title">ToTTo: A Controlled Table-To-Text Generation Dataset</p>
        <p class="paper_authors">Ankur P. Parikh, Xuezhi Wang, Sebastian Gehrmann, Manaal Faruqui, Bhuwan Dhingra, Diyi Yang, and Dipanjan Das</p>
        <p class="paper_venue">EMNLP, 2020. <a href="https://arxiv.org/abs/2004.14373"><u>[pdf]</u></a></p>
      </li>
      <li class="paper_wrapper_all">
        <p class="paper_title">Examining the Ordering of Rhetorical Strategies in Persuasive Requests</p>
        <p class="paper_authors">Omar Shaikh, Jiaao Chen, Jon Saad-Falcon, Polo Chau and Diyi Yang</p>
        <p class="paper_venue">EMNLP (Findings), 2020. <a href="https://arxiv.org/abs/2010.04625"><u>[pdf]</u></a><a href="https://www.cc.gatech.edu/news/641253/being-polite-can-be-essential-getting-loan"><u>[news]</u></a></p>
      </li>
    <li class="paper_wrapper_selected">
        <p class="paper_title">MixText: Linguistically-Informed Interpolation of Hidden Space for Semi-Supervised Text Classification</p>
        <p class="paper_authors">Jiaao Chen, Zichao Yang, and Diyi Yang</p>
        <p class="paper_venue">ACL, 2020, <a href="docs/mixtext_acl_2020.pdf"><u>[pdf]</u></a></p>
      </li>
    <li class="paper_wrapper_selected">
        <p class="paper_title">Characterizing Collective Attention via Descriptor Context: A Case Study of Public Discussions of Crisis Events</p>
        <p class="paper_authors">Ian Stewart, Diyi Yang,  and Jacob Eisenstein</p>
        <p class="paper_venue">ICWSM, 2020, <a href="https://arxiv.org/abs/1909.08784"><u>[pdf]</u></a></p>
      </li>
    <li class="paper_wrapper_selected">
        <p class="paper_title">Automatically Neutralizing Subjective Bias in Text</p>
        <p class="paper_authors">Reid Pryzant, Richard Diehl Martinez, Nathan Dass, Sadao Kurohashi, Dan Jurafsky, and Diyi Yang</p>
        <p class="paper_venue">AAAI, 2020, oral <a href="https://arxiv.org/abs/1911.09709"><u>[pdf]</u></a></p>
      </li>
      <li class="paper_wrapper_all">
        <p class="paper_title">Successful Online Socialization: Lessons from the Wikipedia Education Program</p>
        <p class="paper_authors">Ang Li, Zheng Yao, Diyi Yang, Chinmay Kulkarni, Rosta Farzan, Robert Kraut</p>
        <p class="paper_venue">CSCW, 2020 <a href="docs/cscw_li_2020_wiki.pdf"><u>[pdf]</u></a></p>
        <p class="paper_note">Best Paper Honorable Mention</p>
      </li>
      <li class="paper_wrapper_all">
        <p class="paper_title">Multi-level Modeling of Social Roles in Online Micro-lending Platforms</p>
        <p class="paper_authors">Lu Sun, Robert Kraut, and Diyi Yang</p>
        <p class="paper_venue">CSCW, 2019 <a href="docs/cscw19_sun.pdf"><u>[pdf]</u></a></p>
      </li>
    <li class="paper_wrapper_selected">
        <p class="paper_title">Modeling Persuasive Strategies via Semi-Supervised Neural Nets on Crowdfunding Platforms</p>
        <p class="paper_authors"><span class="me">Diyi Yang</span>*, Jiaao Chen*, Zichao Yang, Dan Jurafsky, and Eduard Hovy</p>
        <p class="paper_venue">NAACL, 2019, oral <a href="docs/naacl19.pdf"><u>[pdf]</u></a></p>
      </li>
    <li class="paper_wrapper_selected">
        <p class="paper_title">Seekers, Providers, Welcomers, and Storytellers: Modeling Social Roles in Online Health Communities</p>
        <p class="paper_authors"><span class="me">Diyi Yang</span>, Robert Kraut, Tenbroeck Smith, Elijah Mayfield, and Dan Jurafsky </p>
        <p class="paper_venue">CHI, 2019 <a href="docs/chi19_social_roles.pdf"><u>[pdf]</u></a> <a href="data/csn_role_interview_instruction.pdf"><u>[supplement]</u></a></p>
        <p class="paper_note">Best Paper Honorable Mention</p>
      </li>
    <li class="paper_wrapper_selected">
        <p class="paper_title">The Channel Matters: Self-disclosure, Reciprocity and Social Support in Online Cancer Support Groups</p>
        <p class="paper_authors"><span class="me">Diyi Yang</span>, Zheng Yao, Joseph Seering, and Robert Kraut </p>
        <p class="paper_venue">CHI, 2019 <a href="docs/chi19_self_disclosure.pdf"><u>[pdf]</u></a></p>
        <p class="paper_note">Best Paper Honorable Mention</p>
      </li>
    <li class="paper_wrapper_all">
        <p class="paper_title">Persuading Teammates to Give: Systematic versus Heuristic Cues for Soliciting Loans</p>
        <p class="paper_authors"><span class="me">Diyi Yang</span> and Robert Kraut</p>
        <p class="paper_venue">CSCW, 2018. <a href="docs/cscw18.pdf"><u>[pdf]</u></a></p>
      </li>
    <li class="paper_wrapper_selected">
        <p class="paper_title">Identifying Semantic Edit Intentions from Revisions in Wikipedia</p>
        <p class="paper_authors"><span class="me">Diyi Yang</span>, Aaron Halfaker, Robert Kraut and Eduard Hovy</p>
        <p class="paper_venue">EMNLP, 2017. <a href="docs/emnlp17.pdf"><u>[pdf]</u></a> <a href="https://github.com/diyiy/Wiki_Semantic_Intention/blob/master/edit_intention_dataset.csv"><u>[data]</u></a></p>
      </li>
     <li class="paper_wrapper_selected">
        <p class="paper_title">Commitment of Newcomers and Old-timers to Online Health Support Communities</p>
        <p class="paper_authors"><span class="me">Diyi Yang</span>, Robert Kraut and John Levine</p>
        <p class="paper_venue">CHI, 2017. <a href="docs/chi17.pdf"><u>[pdf]</u></a></p>
      </li>
     <li class="paper_wrapper_selected">
        <p class="paper_title">Who does What: Editor Role Identification in Wikipedia</p>
        <p class="paper_authors"><span class="me">Diyi Yang</span>, Aaron Halfaker, Robert Kraut and Eduard Hovy</p>
        <p class="paper_venue">ICWSM, 2016. <a href="docs/icwsm2016.pdf"><u>[pdf]</u></a></p>
        <p class="paper_note">Best Paper Honorable Mention</p>
        <p class="paper_venue">In the news: <a href="https://www.lti.cs.cmu.edu/news/yangs-paper-highlights-who-does-what-wikipedia"><u>[CMU LTI]</u></a>, <a href="https://blog.wikimedia.org/2016/05/03/research-newsletter-april-2016/"><u>[Wikimedia Newsletter]</u></a></p>
      </li>
      <li class="paper_wrapper_selected">
        <p class="paper_title">Hierarchical Attention Networks for Document Classification</p>
        <p class="paper_authors">Zichao Yang, <span class="me">Diyi Yang</span>, Chris Dyer, Xiaodong He, Alex Smola and Eduard Hovy  </p>
        <p class="paper_venue"> NAACL, 2016. <a href="docs/naacl16.pdf"><u>[pdf]</u></a> </p>
      </li>
      <li class="paper_wrapper_all">
        <p class="paper_title">Exploring the Effect of Student Confusion in Massive Open Online Courses</p>
        <p class="paper_authors"><span class="me">Diyi Yang</span>, Robert Kraut and Carolyn Rose </p>
        <p class="paper_venue">Journal of Educational Data Mining (JEDM). <a href="docs/jedm.pdf"><u>[pdf]</u></a> </p>
      </li>
      <li class="paper_wrapper_all">
        <p class="paper_title">Humor Recognition and Humor Anchor Extraction</p>
        <p class="paper_authors"><span class="me">Diyi Yang</span>, Alon Lavie, Chris Dyer and Eduard Hovy</p>
        <p class="paper_venue">EMNLP 2015, oral. <a href="docs/emnlp_yang_16.pdf"><u>[pdf]</u></a></p>
      </li>
      <li class="paper_wrapper_all">
        <p class="paper_title">Weakly Supervised Role Identification in Teamwork Interactions</p>
        <p class="paper_authors"><span class="me">Diyi Yang</span>, Miaomiao Wen, Carolyn Rosé </p>
        <p class="paper_venue">ACL 2015, oral. <a href="docs/acl15.pdf"><u>[pdf]</u></a></p>
      </li>
      <li class="paper_wrapper_all">
        <p class="paper_title">That's So Annoying!!!: A Lexical and Frame-Semantic Embedding Based Data Augmentation Approach to Automatic Categorization of Annoying Behaviors using #petpeeve Tweets</p>
        <p class="paper_authors">William Yang Wang, <span class="me">Diyi Yang</span></p>
        <p class="paper_venue">EMNLP 2015. <a href="docs/emnlp_wang_2015.pdf"><u>[pdf]</u></a> <a href="data/petpeeves.zip"><u>[data]</u></a></p>
        <p class="paper_note">Notable Data Set Award</p>
      </li>
      <li class="paper_wrapper_all">
        <p class="paper_title">Incorporating Word Correlation Knowledge into Topic Modeling</p>
        <p class="paper_authors">Pengtao Xie, <span class="me">Diyi Yang</span>, Eric Xing </p>
        <p class="paper_venue">NAACL, 2015. <a href="docs/naacl15.pdf"><u>[pdf]</u></a></p>
      </li>
      <li class="paper_wrapper_all">
        <p class="paper_title">Local Implicit Feedback Mining for Music Recommendation</p>
        <p class="paper_authors"><span class="me">Diyi Yang</span>, Tianqi Chen, Weinan Zhang, Qiuxia Lu, Yong Yu </p>
        <p class="paper_venue">RecSys 2012. <a href="docs/recsys12.pdf"><u>[pdf]</u></a></p>
      </li>
    </ul>
    <h2>Workshops and Posters</h2>
    <ul>
      <li class="paper_wrapper_all">
        <p class="paper_title">Personalized Response Generation with Tensor Factorization</p>
        <p class="paper_authors">Zhenghui Wang, Lingxiao Luo, Diyi Yang</p>
        <p class="paper_venue">The GEM workshop at ACL 2021. <a href="https://aclanthology.org/2021.gem-1.5/"><u>[pdf]</u></a></p>
      </li>
     <li class="paper_wrapper_all">
        <p class="paper_title">The GEM Benchmark: Natural Language Generation, its Evaluation and Metrics</p>
        <p class="paper_authors">The GEM Team</p>
        <p class="paper_venue">The GEM workshop at ACL 2021. <a href="https://aclanthology.org/2021.gem-1.10/"><u>[pdf]</u></a></p>
      </li>
     <li class="paper_wrapper_selected">
        <p class="paper_title">Putting Humans in the Natural Language Processing Loop: A Survey</p>
        <p class="paper_authors"> Zijie Wang, Dongjin Choi, Shenyu Xu, Diyi Yang</p>
        <p class="paper_venue">HCI+NLP workshop at EACL 2021. <a href="https://arxiv.org/abs/2103.04044"><u>[pdf]</u></a></p>
      </li>
     <li class="paper_wrapper_selected">
        <p class="paper_title">This is a Problem, Don’t You Agree? Framing and Bias in Human Evaluation for Natural Language Generation</p>
        <p class="paper_authors">Stephanie Schoch, <span class="me">Diyi Yang</span>, Yangfeng Ji</p>
        <p class="paper_venue">Workshop on Evaluating NLG Evaluation at INLG 2020. <a href="https://evalnlg-workshop.github.io/papers/EvalNLGEval_2020_paper_6.pdf"><u>[pdf]</u></a></p>
      </li>
    </ul>
  </div>"""
soup = BeautifulSoup(html_content, 'html.parser')

def create_markdown_file(folder_name, file_name, content):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    with open(os.path.join(folder_name, file_name), 'w') as file:
        file.write(content)

for li in soup.find_all('li', class_='paper_wrapper_selected'):
    title = li.find('p', class_='paper_title').get_text(strip=True)
    authors = [author.strip() for author in li.find('p', class_='paper_authors').get_text(strip=True).split(",")]
    venue_year = li.find('p', class_='paper_venue').get_text(strip=True)
    year = venue_year.split(",")[-1].split(".")[0].strip()
    venue = venue_year.split(",")[0].strip()
    pdf_link = li.find('a', href=True)['href']
    
    note = li.find('p', class_='paper_note')
    note_text = note.get_text(strip=True) if note else ""
    
    first_author_last_name = authors[0].split(" ")[-1]
    one_word_title = title.split(" ")[0]
    folder_name = f"{first_author_last_name}-{one_word_title}-{year}"
    file_name = "index.md"
    
    markdown_content = f"""---
title: "{title}"
authors:
  - {authors}
categories: []
date: "{year}-01-01"
preprint: false
conference: "{venue}"
paper: {pdf_link}
code:
webpage:
award: "{note_text}"
---"""
    
    create_markdown_file(folder_name, file_name, markdown_content)

    print(f"Generated {folder_name}/{file_name}")