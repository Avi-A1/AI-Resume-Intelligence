from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet


def create_resume_report(
    username,
    prediction,
    score,
    confidence,
    skills,
    missing,
    readiness,
    feedback
):

    file_name = (
        f"{username}_resume_report.pdf"
    )

    doc = SimpleDocTemplate(
        file_name
    )

    styles = getSampleStyleSheet()

    story = []

    # Title
    title = Paragraph(
        "AI Resume Analysis Report",
        styles["Title"]
    )

    story.append(title)
    story.append(
        Spacer(1, 12)
    )

    # Username
    story.append(
        Paragraph(
            f"<b>User:</b> {username}",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"<b>Predicted Role:</b> {prediction}",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"<b>ATS Score:</b> {score}%",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"<b>Confidence:</b> {confidence}%",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"<b>Career Readiness:</b> {readiness}%",
            styles["BodyText"]
        )
    )

    story.append(
        Spacer(1, 15)
    )

    # Skills
    story.append(
        Paragraph(
            "Detected Skills",
            styles["Heading2"]
        )
    )

    for skill in skills:

        story.append(
            Paragraph(
                f"• {skill}",
                styles["BodyText"]
            )
        )

    story.append(
        Spacer(1, 10)
    )

    # Missing Skills
    story.append(
        Paragraph(
            "Skill Gaps",
            styles["Heading2"]
        )
    )

    if missing:

        for skill in missing:

            story.append(
                Paragraph(
                    f"• {skill}",
                    styles["BodyText"]
                )
            )

    else:

        story.append(
            Paragraph(
                "No major skill gaps found.",
                styles["BodyText"]
            )
        )

    story.append(
        Spacer(1, 10)
    )

    # Feedback
    story.append(
        Paragraph(
            "Resume Feedback",
            styles["Heading2"]
        )
    )

    for item in feedback:

        story.append(
            Paragraph(
                f"• {item}",
                styles["BodyText"]
            )
        )

    doc.build(story)

    return file_name