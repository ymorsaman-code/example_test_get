import fitz, os

pdf = '/Users/mac/Downloads/Chapter#06 - Text 2 Speech and Signal Processing.pdf'
doc = fitz.open(pdf)
os.makedirs("out_pdf/text", exist_ok=True)
os.makedirs("out_pdf/images", exist_ok=True)

# Metadata
m = doc.metadata
print(f"Size: {os.path.getsize(pdf)/1024:.1f}KB | Pages: {doc.page_count} | Title: {m['title']} | Author: {m['author']}")

# Text + Images
for i, page in enumerate(doc):
    open(f"out_pdf/text/page_{i+1}.txt", "w").write(page.get_text())
    for j, img in enumerate(page.get_images()):
        pix = fitz.Pixmap(doc, img[0])
        pix.save(f"out_pdf/images/p{i+1}_img{j+1}.png")