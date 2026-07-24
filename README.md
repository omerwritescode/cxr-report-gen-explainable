# Automated Chest X-Ray Report Generation with XAI

> ⚠️ \\\*\\\*Status: Work in Progress.\\\*\\\* This project is under active development (originally scoped as a one-week build). Core pipeline components are being implemented incrementally — see \\\[Progress](#progress) below for what's done vs. pending. Expect breaking changes, incomplete modules, and rough edges until a stable release is tagged.

## Overview

Most automated chest X-ray analysis tools stop at **classification** — flagging whether a finding (e.g. pneumonia, cardiomegaly, effusion) is present or absent. That gives a label, but not the kind of reasoned, free-text report a radiologist would actually write, and it rarely shows *why* the model reached its conclusion.

This project targets that gap directly: an end-to-end pipeline that

* **Generates free-text radiology reports** from chest X-ray images (not just multi-label predictions), and
* **Visually grounds those predictions** using Grad-CAM, so the regions of the image driving the model's output are interpretable rather than a black box.

The goal is a system that produces both *what* the model thinks it sees and *where* it's looking to decide that — closer to how a report actually gets written and reviewed.

## Approach

* **Dataset:** [MIMIC-CXR-JPG](https://physionet.org/content/mimic-cxr-jpg/) (PhysioNet-credentialed access required)
* **Report generation / language modeling:** ClinicalBERT
* **Explainability:** Grad-CAM, overlaid on input X-rays to highlight regions influencing the model's output
* **Framework:** PyTorch
* **Demo:** Gradio / Streamlit interface for interactive inference (upload an X-ray → get a generated report + Grad-CAM heatmap)
* **Hardware:** Developed and trained on a single RTX 5050 laptop GPU

## Fallback plan

Full report generation is the harder, higher-payoff target. If the generation head doesn't converge reliably within the project timeline, the pipeline falls back to a **multi-label classification + Grad-CAM** setup — predicting discrete findings as labels while preserving the visual explainability component. This ensures there's always a working, interpretable end-to-end demo even if free-text generation quality isn't production-ready yet.

## Progress

|Component|Status|
|-|-|
|PhysioNet / MIMIC-CXR-JPG data access|✅ Done|
|Data preprocessing pipeline|🔄 In progress|
|Classification baseline (fallback path)|🔄 In progress|
|Grad-CAM integration|⬜ Not started|
|ClinicalBERT report generation head|⬜ Not started|
|Evaluation (classification + generation metrics)|⬜ Not started|
|Gradio/Streamlit demo|⬜ Not started|

*(Update this table as milestones land — it's the fastest way for a reviewer to see real status at a glance.)*

## Repository structure

```
├── data/               # Data loading \\\& preprocessing scripts (raw data not included — see below)
├── models/             # Model definitions (classification head, report generation head)
├── explainability/      # Grad-CAM implementation and visualization utilities
├── notebooks/           # Exploratory analysis and experiment notebooks
├── demo/                # Gradio/Streamlit app
├── requirements.txt
└── README.md
```

*(Adjust to match your actual layout once it stabilizes.)*

## Setup

```bash
git clone https://github.com/<your-username>/cxr-report-gen-explainable.git
cd cxr-report-gen-explainable
pip install -r requirements.txt
```

**Data access:** MIMIC-CXR-JPG requires a credentialed PhysioNet account and completion of the required data use agreement. This repo does not redistribute the dataset — see the [MIMIC-CXR-JPG page](https://physionet.org/content/mimic-cxr-jpg/) for access instructions.

## Roadmap

* \[ ] Finalize preprocessing and train/val/test splits
* \[ ] Train and validate classification baseline
* \[ ] Integrate Grad-CAM visualizations for baseline
* \[ ] Implement and train report generation head
* \[ ] Compare generation vs. classification+Grad-CAM fallback on held-out set
* \[ ] Ship interactive demo

## Motivation

This project is part of an MSc Data Science portfolio, built to demonstrate applied skills in medical imaging, multimodal (vision + language) modeling, and model interpretability — with an eye toward AI Engineer roles.

## License

*(Add a license once you decide — MIT is a common default for portfolio projects.)*

