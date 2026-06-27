# Iqbal Ahdagita Elbadra - Professional Portfolio Website

Welcome to my personal portfolio website repository. This site showcases my work, projects, and career history as a **Software Engineer, Data Scientist, and Machine Learning Specialist**.

🔗 **Live Website:** [iqbalahdagita.web.id](https://iqbalahdagita.web.id)

---

## 🚀 Key Features

*   **Premium Single-Page Portfolio:** A modern, clean, and responsive design presenting projects, technical skills, career timeline, and academic background.
*   **ATS-Friendly CV System:** Built-in HTML CV template (`cv.html`) that can be compiled natively into a text-selectable, ATS-optimized PDF.
*   **Project Showcase:** Exhibits advanced projects in GenAI, RAG pipelines, Web Crawling, and traditional Full-Stack applications.

---

## 🛠️ Tech Stack & Plugins

*   **Core:** HTML5, Vanilla CSS, JavaScript.
*   **Frameworks & Libraries:** Bootstrap 5, jQuery.
*   **UI/UX Plugins:** OwlCarousel2 (Sliders), Lity (Lightboxes), SpinKit (Loaders), FontAwesome v6.
*   **Automation:** Python scripts for PDF generation and verification.

---

## 📄 Automated CV Generation & Verification

This project features a script that automates the generation of the PDF CV directly from the HTML source to ensure it remains 100% updated with the website content.

### Prerequisites
*   Python 3.x
*   Microsoft Edge (installed in default Windows paths)
*   Python package: `pypdf` (only needed for verification)

### Steps:

1.  **Modify CV Content:**
    Edit the content inside `cv.html` to update your CV.

2.  **Generate the PDF:**
    Run the generation script:
    ```bash
    python generate_pdf.py
    ```
    This script launches Microsoft Edge in headless mode to natively print `cv.html` into a high-quality, text-selectable PDF named `CVIQBALCOMPLETE.pdf`.

3.  **Verify ATS Readability:**
    Verify that the PDF text remains selectable and compatible with Applicant Tracking Systems (ATS):
    ```bash
    python extract_pdf_v2.py
    ```

---

## 📂 Project Structure

```
├── assets/                     # Fonts and static assets
├── blog/                       # Blog post HTML pages
├── images/                     # Project screenshots, logos, and illustrations
├── js/                         # JavaScript source files
├── plugins/                    # UI/UX plugins (OwlCarousel, Lity, etc.)
├── styles/                     # CSS stylesheets (Bootstrap & custom styles)
├── cv.html                     # HTML source for the CV PDF
├── index.html                  # Main portfolio website page
├── CVIQBALCOMPLETE.pdf         # The active downloadable CV PDF
├── generate_pdf.py             # Python script to compile cv.html -> PDF
└── extract_pdf_v2.py           # Python script to test PDF text extraction
```

---

## 💻 Contact & Socials

*   **Email:** [spfindo@gmail.com](mailto:spfindo@gmail.com)
*   **LinkedIn:** [linkedin.com/in/iqbal-ahdagita](https://linkedin.com/in/iqbal-ahdagita)
*   **Instagram:** [@iqbal.ahdagita](https://www.instagram.com/iqbal.ahdagita/)
