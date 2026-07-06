from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def create_pdf(
    filename,
    area,
    bedrooms,
    bathrooms,
    stories,
    parking,
    prediction
):

    styles = getSampleStyleSheet()

    pdf = SimpleDocTemplate(filename)

    story = []

    story.append(Paragraph("<b>House Price Prediction Report</b>", styles['Title']))

    story.append(Paragraph(f"Area : {area} sq.ft", styles['BodyText']))
    story.append(Paragraph(f"Bedrooms : {bedrooms}", styles['BodyText']))
    story.append(Paragraph(f"Bathrooms : {bathrooms}", styles['BodyText']))
    story.append(Paragraph(f"Stories : {stories}", styles['BodyText']))
    story.append(Paragraph(f"Parking : {parking}", styles['BodyText']))

    story.append(Paragraph("<br/>", styles['BodyText']))

    story.append(
        Paragraph(
            f"<b>Predicted House Price : ₹ {prediction:,.2f}</b>",
            styles['Heading2']
        )
    )

    pdf.build(story)
