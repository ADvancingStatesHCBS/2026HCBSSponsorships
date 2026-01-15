#!/usr/bin/env python3
"""
KDADS Policy Manual Project - Monday.com Sequential Setup Guide
PDF Generator with Interactive Checkboxes
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, black, white
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, ListFlowable, ListItem
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.pdfbase import pdfform
from reportlab.platypus.flowables import Flowable

# Colors
PRIMARY_BLUE = HexColor('#0086c0')
HEADER_BLUE = HexColor('#1a365d')
LIGHT_GRAY = HexColor('#f7fafc')
BORDER_GRAY = HexColor('#e2e8f0')
TEXT_GRAY = HexColor('#2d3748')

class CheckBox(Flowable):
    """Interactive checkbox flowable"""
    def __init__(self, name, checked=False, size=10):
        Flowable.__init__(self)
        self.name = name
        self.checked = checked
        self.size = size
        self.width = size
        self.height = size

    def draw(self):
        self.canv.saveState()
        form = self.canv.acroForm
        form.checkbox(
            name=self.name,
            tooltip=self.name,
            x=0,
            y=0,
            size=self.size,
            buttonStyle='check',
            borderColor=black,
            fillColor=white,
            textColor=black,
            forceBorder=True,
            checked=self.checked
        )
        self.canv.restoreState()

class CheckboxItem(Flowable):
    """A checkbox with text next to it"""
    def __init__(self, name, text, styles, checked=False, indent=0):
        Flowable.__init__(self)
        self.name = name
        self.text = text
        self.styles = styles
        self.checked = checked
        self.indent = indent
        self.checkbox_size = 10
        self.spacing = 5

    def wrap(self, availWidth, availHeight):
        self.width = availWidth
        self.height = 18
        return (self.width, self.height)

    def draw(self):
        self.canv.saveState()

        # Draw checkbox
        x_pos = self.indent
        form = self.canv.acroForm
        form.checkbox(
            name=self.name,
            tooltip=self.text[:50] if len(self.text) > 50 else self.text,
            x=x_pos,
            y=2,
            size=self.checkbox_size,
            buttonStyle='check',
            borderColor=black,
            fillColor=white,
            textColor=black,
            forceBorder=True,
            checked=self.checked
        )

        # Draw text
        self.canv.setFont('Helvetica', 9)
        self.canv.setFillColor(TEXT_GRAY)
        text_x = x_pos + self.checkbox_size + self.spacing
        self.canv.drawString(text_x, 4, self.text[:100] + ('...' if len(self.text) > 100 else ''))

        self.canv.restoreState()

def create_styles():
    """Create custom paragraph styles"""
    styles = getSampleStyleSheet()

    styles.add(ParagraphStyle(
        name='Title1',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=HEADER_BLUE,
        spaceAfter=20,
        spaceBefore=10,
        alignment=TA_CENTER
    ))

    styles.add(ParagraphStyle(
        name='Phase',
        parent=styles['Heading1'],
        fontSize=16,
        textColor=PRIMARY_BLUE,
        spaceAfter=12,
        spaceBefore=20,
        borderColor=PRIMARY_BLUE,
        borderWidth=1,
        borderPadding=5
    ))

    styles.add(ParagraphStyle(
        name='Section',
        parent=styles['Heading2'],
        fontSize=13,
        textColor=HEADER_BLUE,
        spaceAfter=8,
        spaceBefore=15
    ))

    styles.add(ParagraphStyle(
        name='SubSection',
        parent=styles['Heading3'],
        fontSize=11,
        textColor=TEXT_GRAY,
        spaceAfter=6,
        spaceBefore=10,
        fontName='Helvetica-Bold'
    ))

    styles.add(ParagraphStyle(
        name='BodyContent',
        parent=styles['Normal'],
        fontSize=9,
        textColor=TEXT_GRAY,
        spaceAfter=6,
        leading=12
    ))

    styles.add(ParagraphStyle(
        name='Note',
        parent=styles['Normal'],
        fontSize=8,
        textColor=HexColor('#718096'),
        spaceAfter=6,
        fontName='Helvetica-Oblique'
    ))

    styles.add(ParagraphStyle(
        name='TableHeader',
        parent=styles['Normal'],
        fontSize=8,
        textColor=white,
        fontName='Helvetica-Bold',
        alignment=TA_CENTER
    ))

    styles.add(ParagraphStyle(
        name='TableCell',
        parent=styles['Normal'],
        fontSize=8,
        textColor=TEXT_GRAY,
        leading=10
    ))

    return styles

def create_checkbox_item(checkbox_counter, text, styles, indent=0):
    """Create a checkbox item flowable"""
    name = f"checkbox_{checkbox_counter[0]}"
    checkbox_counter[0] += 1
    return CheckboxItem(name, text, styles, indent=indent)

def build_document():
    """Build the complete PDF document"""
    doc = SimpleDocTemplate(
        "/home/user/2026HCBSSponsorships/KDADS-Monday-Setup-Guide.pdf",
        pagesize=letter,
        rightMargin=0.5*inch,
        leftMargin=0.5*inch,
        topMargin=0.5*inch,
        bottomMargin=0.5*inch
    )

    styles = create_styles()
    story = []
    checkbox_counter = [1]  # Use list to allow mutation in nested function

    def cb(text, indent=0):
        """Shorthand for creating checkbox items"""
        return create_checkbox_item(checkbox_counter, text, styles, indent)

    def add_header(text):
        story.append(Paragraph(text, styles['Phase']))

    def add_section(text):
        story.append(Paragraph(text, styles['Section']))

    def add_subsection(text):
        story.append(Paragraph(text, styles['SubSection']))

    def add_text(text):
        story.append(Paragraph(text, styles['BodyContent']))

    def add_note(text):
        story.append(Paragraph(text, styles['Note']))

    def add_space(height=10):
        story.append(Spacer(1, height))

    # ========== TITLE PAGE ==========
    story.append(Spacer(1, 1*inch))
    story.append(Paragraph("KDADS Policy Manual Project", styles['Title1']))
    story.append(Paragraph("Monday.com Sequential Setup Guide", styles['Title1']))
    story.append(Spacer(1, 0.5*inch))
    story.append(Paragraph("Interactive Checklist with Checkable Boxes", styles['Section']))
    story.append(Spacer(1, 0.3*inch))
    story.append(Paragraph("Document Version: 1.0 | Created: January 2026", styles['Note']))
    story.append(PageBreak())

    # ========== TABLE OF CONTENTS ==========
    story.append(Paragraph("Table of Contents", styles['Phase']))
    toc_items = [
        "Phase 0: Pre-Setup Preparation",
        "Phase 1: Workspace Configuration",
        "Phase 2: Board 1 - Stakeholder Engagement - Delphi",
        "Phase 3: Board 2 - Stakeholder Engagement - Workgroup",
        "Phase 4: Board 3 - Stakeholder Engagement - Draft and Review",
        "Phase 5: Board 4 - Contract Deliverables Tracker",
        "Phase 6: Cross-Board Configuration",
        "Phase 7: Automations Setup",
        "Phase 8: Views and Dashboard Creation",
        "Phase 9: Final Validation and Testing",
        "Appendix A: Status Labels Quick Reference",
        "Appendix B: Responsible Party Reference",
        "Appendix C: Deliverables Timeline Reference",
        "Appendix D: Troubleshooting Guide"
    ]
    for i, item in enumerate(toc_items):
        story.append(Paragraph(f"{i+1}. {item}", styles['BodyText']))
    story.append(PageBreak())

    # ========== PHASE 0 ==========
    add_header("Phase 0: Pre-Setup Preparation")

    add_section("0.1 Account & Access Verification")
    story.append(cb("Confirm Monday.com account has appropriate plan level (Pro or Enterprise recommended)"))
    story.append(cb("Verify admin access to create boards and workspaces"))
    story.append(cb("Collect email addresses for all team members (ADS and KDADS staff)"))
    story.append(cb("Determine who needs Owner vs. Member vs. Viewer access"))

    add_section("0.2 Gather Required Information")
    story.append(cb("Finalize list of policy topics for Board 3 (Draft and Review) - currently TBD"))
    story.append(cb("Confirm target dates for Phase A-D deliverables"))
    story.append(cb("Identify primary Owner assignments for each policy topic"))
    story.append(cb("Validate the 75% consensus threshold for Delphi process"))

    add_section("0.3 Document Naming Conventions")
    story.append(cb("Establish naming convention for boards (e.g., 'KDADS - [Board Name]')"))
    story.append(cb("Establish naming convention for groups (policy topics)"))
    story.append(cb("Establish color coding scheme for status labels"))

    story.append(PageBreak())

    # ========== PHASE 1 ==========
    add_header("Phase 1: Workspace Configuration")

    add_section("1.1 Create Workspace")
    story.append(cb("Navigate to Monday.com -> Workspaces"))
    story.append(cb("Click 'Add Workspace'"))
    story.append(cb("Name: 'KDADS Policy Manual Project'"))
    story.append(cb("Set workspace icon (optional - suggest policy/document icon)"))
    story.append(cb("Set workspace description"))

    add_section("1.2 Configure Workspace Settings")
    story.append(cb("Set workspace to 'Main' or 'Open' depending on visibility needs"))
    story.append(cb("Add workspace members - All ADS team members"))
    story.append(cb("Add workspace members - All KDADS team members"))
    story.append(cb("Add workspace members - External stakeholders (view access)"))

    add_section("1.3 Create Standardized Status Labels Template")
    add_text("Document these labels for consistent use across all boards:")

    status_data = [
        ['Label', 'Color Code', 'Usage'],
        ['Not Started', 'Gray (#c4c4c4)', 'Default state'],
        ['In Progress', 'Blue (#0086c0)', 'Active work'],
        ['Pending Review', 'Yellow (#fdab3d)', 'Awaiting review'],
        ['Blocked', 'Red (#e2445c)', 'Cannot proceed'],
        ['Complete', 'Green (#00c875)', 'Finished']
    ]

    status_table = Table(status_data, colWidths=[1.5*inch, 1.5*inch, 3*inch])
    status_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), PRIMARY_BLUE),
        ('TEXTCOLOR', (0, 0), (-1, 0), white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('TOPPADDING', (0, 0), (-1, 0), 8),
        ('BACKGROUND', (0, 1), (-1, -1), LIGHT_GRAY),
        ('GRID', (0, 0), (-1, -1), 0.5, BORDER_GRAY),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    story.append(status_table)

    story.append(PageBreak())

    # ========== PHASE 2 ==========
    add_header("Phase 2: Board 1 - Stakeholder Engagement - Delphi")

    add_section("2.1 Create Board")
    story.append(cb("Click 'Add' -> 'New Board'"))
    story.append(cb("Select 'Start from scratch'"))
    story.append(cb("Name: 'Stakeholder Engagement - Delphi'"))
    story.append(cb("Set board type: Main Board"))
    story.append(cb("Set board permissions: Private (ADS and KDADS only)"))

    add_section("2.2 Create Groups (Policy Topics)")
    story.append(cb("Group 1: Provision of Direct Services"))
    story.append(cb("Group 2: Client Eligibility"))
    story.append(cb("Group 3: Client and Service Priority"))
    story.append(cb("Group 4: GESN/Targeting"))
    story.append(cb("Set group colors for visual separation"))

    add_section("2.3 Create Process Stage Columns (Status Type)")
    add_text("Delete any default columns, then create in order:")
    story.append(cb("1. In-Person Kickoff - Labels: Not Started, In Progress, Complete"))
    story.append(cb("2. First Meeting - Problem ID - Labels: Not Started, In Progress, Complete"))
    story.append(cb("3. Second Meeting - Solutions/Goals - Labels: Not Started, In Progress, Complete"))
    story.append(cb("4. Survey Development & Iteration - Labels: Not Started, In Progress, Pending Review, Complete"))
    story.append(cb("5. Policy Drafting - Labels: Not Started, In Progress, Complete"))
    story.append(cb("6. Policy Review - Labels: Not Started, In Progress, Pending Review, Complete"))
    story.append(cb("7. Finalize Language - Labels: Not Started, In Progress, Complete"))
    story.append(cb("8. Legal Review - Labels: Not Started, In Progress, Pending Review, Blocked, Complete"))
    story.append(cb("9. Language Updates (if needed) - Labels: Not Needed, Not Started, In Progress, Complete"))
    story.append(cb("10. Commissioner Sign-Off & Publish - Labels: Not Started, In Progress, Complete"))

    add_section("2.4 Create Additional Columns")
    story.append(cb("Owner (People) - Allow multiple people"))
    story.append(cb("Due Date (Date) - Enable deadline mode"))
    story.append(cb("Survey Round # (Numbers) - Set unit: none, allow decimals: no"))
    story.append(cb("Consensus % (Numbers) - Set unit: %, range 0-100"))
    story.append(cb("Notes/Blockers (Long Text) - Enable rich text formatting"))
    story.append(cb("Responsible Party (Dropdown) - Options: ADS, KDADS, Both"))

    add_section("2.5 Add Items (Placeholder Rows)")
    story.append(cb("In 'Provision of Direct Services' -> Add item: 'Policy Development Item 1'"))
    story.append(cb("In 'Client Eligibility' -> Add item: 'Policy Development Item 1'"))
    story.append(cb("In 'Client and Service Priority' -> Add item: 'Policy Development Item 1'"))
    story.append(cb("In 'GESN/Targeting' -> Add item: 'Policy Development Item 1'"))

    add_section("2.6 Set Column Descriptions")
    story.append(cb("1. In-Person Kickoff -> 'Establish Delphi group (KDADS & ADS)'"))
    story.append(cb("2. First Meeting - Problem ID -> 'Identify policy problem areas (ADS)'"))
    story.append(cb("3. Second Meeting - Solutions/Goals -> 'Establish potential solutions (ADS)'"))
    story.append(cb("4. Survey Development & Iteration -> 'Iterate until 75% consensus (ADS)'"))
    story.append(cb("5. Policy Drafting -> 'Draft policy language (ADS)'"))
    story.append(cb("6. Policy Review -> 'KDADS review of draft'"))
    story.append(cb("7. Finalize Language -> 'Finalize policy language (ADS)'"))
    story.append(cb("8. Legal Review -> 'Legal review (KDADS)'"))
    story.append(cb("9. Language Updates (if needed) -> 'Conditional on legal feedback (ADS)'"))
    story.append(cb("10. Commissioner Sign-Off & Publish -> 'Terminal stage (KDADS)'"))

    add_section("2.7 Board 1 Verification Checklist")
    story.append(cb("Verify all 4 groups are created"))
    story.append(cb("Verify all 10 status columns exist"))
    story.append(cb("Verify all 6 additional columns exist"))
    story.append(cb("Verify column descriptions are set"))
    story.append(cb("Test adding/editing an item"))

    story.append(PageBreak())

    # ========== PHASE 3 ==========
    add_header("Phase 3: Board 2 - Stakeholder Engagement - Workgroup")

    add_section("3.1 Create Board")
    story.append(cb("Click 'Add' -> 'New Board'"))
    story.append(cb("Select 'Start from scratch'"))
    story.append(cb("Name: 'Stakeholder Engagement - Workgroup'"))
    story.append(cb("Set board type: Main Board"))
    story.append(cb("Set board permissions: Private (ADS and KDADS only)"))

    add_section("3.2 Create Groups (Policy Topics)")
    story.append(cb("Group 1: Area Plans on Aging"))
    story.append(cb("Group 2: AAA Advisory Council"))
    story.append(cb("Group 3: Conflicts of Interest"))
    story.append(cb("Group 4: Title III/VI Coordination"))
    story.append(cb("Group 5: Congregate Nutrition Services"))
    story.append(cb("Group 6: Home Delivered Meals"))
    story.append(cb("Group 7: Grab & Go Nutrition Services"))
    story.append(cb("Group 8: Monitoring"))
    story.append(cb("Group 9: NSIP"))
    story.append(cb("Set group colors (optional)"))

    add_section("3.3 Create Process Stage Columns (Status Type)")
    story.append(cb("1. Initial Policy Drafting - Labels: Not Started, In Progress, Complete"))
    story.append(cb("2. Policy Review - Labels: Not Started, In Progress, Pending Review, Complete"))
    story.append(cb("3. Workgroup Convening - Labels: Not Started, Scheduled, In Progress, Complete"))
    story.append(cb("4. Revise & Finalize Draft - Labels: Not Started, In Progress, Complete"))
    story.append(cb("5. Legal Review - Labels: Not Started, In Progress, Pending Review, Blocked, Complete"))
    story.append(cb("6. Language Updates (if needed) - Labels: Not Needed, Not Started, In Progress, Complete"))
    story.append(cb("7. Commissioner Sign-Off & Publish - Labels: Not Started, In Progress, Complete"))

    add_section("3.4 Create Additional Columns")
    story.append(cb("Owner (People) - Allow multiple people"))
    story.append(cb("Due Date (Date) - Enable deadline mode"))
    story.append(cb("Workgroup Meeting Date (Date) - Standard date picker"))
    story.append(cb("Notes/Blockers (Long Text) - Enable rich text formatting"))
    story.append(cb("Responsible Party (Dropdown) - Options: ADS, KDADS, Both"))

    add_section("3.5 Add Items (Placeholder Rows)")
    story.append(cb("In 'Area Plans on Aging' -> Add item"))
    story.append(cb("In 'AAA Advisory Council' -> Add item"))
    story.append(cb("In 'Conflicts of Interest' -> Add item"))
    story.append(cb("In 'Title III/VI Coordination' -> Add item"))
    story.append(cb("In 'Congregate Nutrition Services' -> Add item"))
    story.append(cb("In 'Home Delivered Meals' -> Add item"))
    story.append(cb("In 'Grab & Go Nutrition Services' -> Add item"))
    story.append(cb("In 'Monitoring' -> Add item"))
    story.append(cb("In 'NSIP' -> Add item"))

    add_section("3.6 Set Column Descriptions")
    story.append(cb("1. Initial Policy Drafting -> 'Initial draft creation (ADS)'"))
    story.append(cb("2. Policy Review -> 'KDADS review of initial draft'"))
    story.append(cb("3. Workgroup Convening -> 'Convene workgroup for collaborative review (ADS)'"))
    story.append(cb("4. Revise & Finalize Draft -> 'Incorporate workgroup feedback (ADS)'"))
    story.append(cb("5. Legal Review -> 'Legal review (KDADS)'"))
    story.append(cb("6. Language Updates (if needed) -> 'Conditional on legal feedback (ADS)'"))
    story.append(cb("7. Commissioner Sign-Off & Publish -> 'Terminal stage (KDADS)'"))

    add_section("3.7 Board 2 Verification Checklist")
    story.append(cb("Verify all 9 groups are created"))
    story.append(cb("Verify all 7 status columns exist"))
    story.append(cb("Verify all 5 additional columns exist"))
    story.append(cb("Verify column descriptions are set"))
    story.append(cb("Test adding/editing an item"))

    story.append(PageBreak())

    # ========== PHASE 4 ==========
    add_header("Phase 4: Board 3 - Stakeholder Engagement - Draft and Review")

    add_section("4.1 Create Board")
    story.append(cb("Click 'Add' -> 'New Board'"))
    story.append(cb("Select 'Start from scratch'"))
    story.append(cb("Name: 'Stakeholder Engagement - Draft and Review'"))
    story.append(cb("Set board type: Main Board"))
    story.append(cb("Set board permissions: Private (ADS and KDADS only)"))

    add_section("4.2 Create Groups (Policy Topics)")
    add_note("Note: Policy topics are TBD - create placeholder groups:")
    story.append(cb("Group 1: TBD Policy Topic 1"))
    story.append(cb("Group 2: TBD Policy Topic 2"))
    story.append(cb("Group 3: TBD Policy Topic 3"))
    add_note("Update these groups once policy topics are finalized")

    add_section("4.3 Create Process Stage Columns (Status Type)")
    story.append(cb("1. Initial Policy Drafting - Labels: Not Started, In Progress, Complete"))
    story.append(cb("2. Policy Review - Labels: Not Started, In Progress, Pending Review, Complete"))
    story.append(cb("3. Revise & Finalize Draft - Labels: Not Started, In Progress, Complete"))
    story.append(cb("4. Legal Review - Labels: Not Started, In Progress, Pending Review, Blocked, Complete"))
    story.append(cb("5. Language Updates (if needed) - Labels: Not Needed, Not Started, In Progress, Complete"))
    story.append(cb("6. Commissioner Sign-Off & Publish - Labels: Not Started, In Progress, Complete"))

    add_section("4.4 Create Additional Columns")
    story.append(cb("Owner (People) - Allow multiple people"))
    story.append(cb("Due Date (Date) - Enable deadline mode"))
    story.append(cb("Notes/Blockers (Long Text) - Enable rich text formatting"))
    story.append(cb("Responsible Party (Dropdown) - Options: ADS, KDADS, Both"))

    add_section("4.5 Add Items (Placeholder Rows)")
    story.append(cb("In each TBD group -> Add item: 'Policy Development Item 1'"))

    add_section("4.6 Set Column Descriptions")
    story.append(cb("1. Initial Policy Drafting -> 'Initial draft creation (ADS)'"))
    story.append(cb("2. Policy Review -> 'KDADS review of initial draft'"))
    story.append(cb("3. Revise & Finalize Draft -> 'Finalize draft based on review (ADS)'"))
    story.append(cb("4. Legal Review -> 'Legal review (KDADS)'"))
    story.append(cb("5. Language Updates (if needed) -> 'Conditional on legal feedback (ADS)'"))
    story.append(cb("6. Commissioner Sign-Off & Publish -> 'Terminal stage (KDADS)'"))

    add_section("4.7 Board 3 Verification Checklist")
    story.append(cb("Verify placeholder groups are created"))
    story.append(cb("Verify all 6 status columns exist"))
    story.append(cb("Verify all 4 additional columns exist"))
    story.append(cb("Verify column descriptions are set"))
    story.append(cb("Test adding/editing an item"))
    story.append(cb("ACTION REQUIRED: Update groups when policy topics are finalized"))

    story.append(PageBreak())

    # ========== PHASE 5 ==========
    add_header("Phase 5: Board 4 - Contract Deliverables Tracker")

    add_section("5.1 Create Board")
    story.append(cb("Click 'Add' -> 'New Board'"))
    story.append(cb("Select 'Start from scratch'"))
    story.append(cb("Name: 'Contract Deliverables Tracker'"))
    story.append(cb("Set board type: Main Board"))
    story.append(cb("Set board permissions: Private (ADS and KDADS only)"))

    add_section("5.2 Create Groups (Contract Phases)")
    story.append(cb("Group 1: Phase A - New Policy & Procedures Manual (Blue)"))
    story.append(cb("Group 2: Phase B - Stakeholder Engagement (Purple)"))
    story.append(cb("Group 3: Phase C - Final Manual Assembly (Orange)"))
    story.append(cb("Group 4: Phase D - Training & Implementation (Green)"))

    add_section("5.3 Create Columns")
    story.append(cb("Deliverable (Text) - Standard text"))
    story.append(cb("Phase (Dropdown) - Options: A, B, C, D"))
    story.append(cb("Status (Status) - Labels: Not Started, In Progress, Pending Review, Blocked, Complete"))
    story.append(cb("Due Date (Date) - Enable deadline mode"))
    story.append(cb("Owner (People) - Allow multiple people"))
    story.append(cb("Dependencies (Link to Item) - Link to items in this board and other boards"))
    story.append(cb("Completion % (Progress Tracking) - Or use Numbers column with % unit"))
    story.append(cb("Key Milestones (Long Text) - Enable rich text formatting"))
    story.append(cb("Notes (Long Text) - Enable rich text formatting"))

    add_section("5.4 Add Deliverable Items - Phase A")
    story.append(cb("Add: 'New Policy & Procedures Manual'"))
    story.append(cb("Add: 'Project Management Hub'"))

    add_section("5.4 Add Deliverable Items - Phase B")
    story.append(cb("Add: 'Initial Drafts Completion' - Due: March 2026"))
    story.append(cb("Add: 'Workgroups Complete' - Due: May 2026"))
    story.append(cb("Add: 'Revisions Complete' - Due: June 2026"))
    story.append(cb("Add: 'Delphi Drafts Complete' - Due: August 2026"))

    add_section("5.4 Add Deliverable Items - Phase C")
    story.append(cb("Add: 'Legal/Leadership Revisions'"))
    story.append(cb("Add: 'Dependency Mapping'"))
    story.append(cb("Add: 'Anchor Policy Identification'"))

    add_section("5.4 Add Deliverable Items - Phase D")
    story.append(cb("Add: 'Workgroup Discussions (3)'"))
    story.append(cb("Add: 'Forms & Job Aids Development'"))
    story.append(cb("Add: 'In-Person Training (1)'"))
    story.append(cb("Add: 'Webinar (1)'"))
    story.append(cb("Add: 'E-Learning Modules'"))

    add_section("5.5 Configure Dependencies")
    story.append(cb("Link Phase B items to relevant policy boards"))
    story.append(cb("Link Phase C items to Phase B completion"))
    story.append(cb("Link Phase D items to Phase C completion"))

    add_section("5.6 Board 4 Verification Checklist")
    story.append(cb("Verify all 4 phase groups are created"))
    story.append(cb("Verify all 9 columns exist"))
    story.append(cb("Verify all deliverable items are added"))
    story.append(cb("Verify dependencies are linked"))
    story.append(cb("Test progress tracking functionality"))

    story.append(PageBreak())

    # ========== PHASE 6 ==========
    add_header("Phase 6: Cross-Board Configuration")

    add_section("6.1 Standardize Status Labels Across All Boards")
    add_text("For each board, verify status columns use consistent labels:")
    story.append(cb("Not Started - Gray (#c4c4c4) - Default state"))
    story.append(cb("In Progress - Blue (#0086c0) - Active work"))
    story.append(cb("Pending Review - Yellow (#fdab3d) - Awaiting review"))
    story.append(cb("Blocked - Red (#e2445c) - Cannot proceed"))
    story.append(cb("Complete - Green (#00c875) - Finished"))
    story.append(cb("Not Needed - Light Gray (#c4c4c4) - For conditional steps"))
    story.append(cb("Scheduled - Purple (#a25ddc) - For meetings/events"))

    add_section("6.2 Configure Board Permissions")
    add_subsection("Board 1 (Delphi):")
    story.append(cb("Set ADS team members as Owners for columns 2, 3, 4, 5, 7, 9"))
    story.append(cb("Set KDADS team members as Owners for columns 1, 6, 8, 10"))

    add_subsection("Board 2 (Workgroup):")
    story.append(cb("Set ADS team members as Owners for columns 1, 3, 4, 6"))
    story.append(cb("Set KDADS team members as Owners for columns 2, 5, 7"))

    add_subsection("Board 3 (Draft and Review):")
    story.append(cb("Set ADS team members as Owners for columns 1, 3, 5"))
    story.append(cb("Set KDADS team members as Owners for columns 2, 4, 6"))

    add_subsection("Board 4 (Deliverables):")
    story.append(cb("Set both ADS and KDADS as board Owners"))

    add_section("6.3 Create Board Connections")
    story.append(cb("Connect Board 4 (Deliverables) to Board 1 (Delphi) via Dependencies column"))
    story.append(cb("Connect Board 4 (Deliverables) to Board 2 (Workgroup) via Dependencies column"))
    story.append(cb("Connect Board 4 (Deliverables) to Board 3 (Draft/Review) via Dependencies column"))

    add_section("6.4 Cross-Board Verification")
    story.append(cb("Verify all boards appear in workspace"))
    story.append(cb("Verify all team members have appropriate access"))
    story.append(cb("Test board connections/links"))

    story.append(PageBreak())

    # ========== PHASE 7 ==========
    add_header("Phase 7: Automations Setup")

    add_section("7.1 Board 1 (Delphi) Automations")
    add_subsection("Automation 1: Notify KDADS on Policy Review")
    story.append(cb("Navigate to Board 1 -> Automations -> Add Automation"))
    story.append(cb("Trigger: When '6. Policy Review' changes to 'In Progress'"))
    story.append(cb("Action: Notify KDADS team members"))
    story.append(cb("Message: 'Policy item ready for KDADS review in Delphi board'"))

    add_subsection("Automation 2: Notify KDADS on Legal Review")
    story.append(cb("Trigger: When '8. Legal Review' changes to 'In Progress'"))
    story.append(cb("Action: Notify KDADS team members"))

    add_subsection("Automation 3: Notify ADS on Language Updates Needed")
    story.append(cb("Trigger: When '9. Language Updates (if needed)' changes to 'Not Started'"))
    story.append(cb("Action: Notify ADS team members"))

    add_subsection("Automation 4: Due Date Reminder")
    story.append(cb("Trigger: When Due Date arrives"))
    story.append(cb("Action: Notify Owner"))

    add_subsection("Automation 5: Approaching Deadline Warning")
    story.append(cb("Trigger: 3 days before Due Date"))
    story.append(cb("Action: Notify Owner"))

    add_section("7.2 Board 2 (Workgroup) Automations")
    add_subsection("Automation 1: Notify KDADS on Policy Review")
    story.append(cb("Trigger: When '2. Policy Review' changes to 'In Progress'"))
    story.append(cb("Action: Notify KDADS team members"))

    add_subsection("Automation 2: Notify KDADS on Legal Review")
    story.append(cb("Trigger: When '5. Legal Review' changes to 'In Progress'"))
    story.append(cb("Action: Notify KDADS team members"))

    add_subsection("Automation 3: Notify ADS on Language Updates Needed")
    story.append(cb("Trigger: When '6. Language Updates (if needed)' changes to 'Not Started'"))
    story.append(cb("Action: Notify ADS team members"))

    add_subsection("Automation 4: Workgroup Meeting Reminder")
    story.append(cb("Trigger: 1 day before Workgroup Meeting Date"))
    story.append(cb("Action: Notify Owner"))

    add_subsection("Automation 5: Due Date Reminder")
    story.append(cb("Trigger: When Due Date arrives"))
    story.append(cb("Action: Notify Owner"))

    add_section("7.3 Board 3 (Draft and Review) Automations")
    story.append(cb("Automation 1: Notify KDADS when '2. Policy Review' changes to 'In Progress'"))
    story.append(cb("Automation 2: Notify KDADS when '4. Legal Review' changes to 'In Progress'"))
    story.append(cb("Automation 3: Notify ADS when '5. Language Updates' changes to 'Not Started'"))
    story.append(cb("Automation 4: Due Date Reminder - Notify Owner"))

    add_section("7.4 Board 4 (Deliverables) Automations")
    story.append(cb("Automation 1: Phase Completion - Notify all when group items complete"))
    story.append(cb("Automation 2: Blocked Item Alert - Notify Owners when Status = 'Blocked'"))
    story.append(cb("Automation 3: Due Date Warning - 7 days before Due Date"))

    add_section("7.5 Automation Verification Checklist")
    story.append(cb("Test each automation by changing status values"))
    story.append(cb("Verify notifications are received by correct team members"))
    story.append(cb("Confirm automation triggers work as expected"))
    story.append(cb("Document any automation failures or issues"))

    story.append(PageBreak())

    # ========== PHASE 8 ==========
    add_header("Phase 8: Views and Dashboard Creation")

    add_section("8.1 Board 1 (Delphi) Views")
    add_subsection("Main Table View (Default)")
    story.append(cb("Verify default table view shows all columns"))
    story.append(cb("Sort by Due Date (ascending)"))
    story.append(cb("Save view as 'Main Table'"))

    add_subsection("Timeline/Gantt View")
    story.append(cb("Click 'Add View' -> 'Timeline'"))
    story.append(cb("Name: 'Delphi Timeline'"))
    story.append(cb("Configure: Date column: Due Date"))
    story.append(cb("Configure: Group by: Policy Topic (groups)"))

    add_subsection("Calendar View")
    story.append(cb("Click 'Add View' -> 'Calendar'"))
    story.append(cb("Name: 'Delphi Calendar'"))
    story.append(cb("Configure: Date column: Due Date"))

    add_subsection("Status Overview (Chart)")
    story.append(cb("Click 'Add View' -> 'Chart'"))
    story.append(cb("Name: 'Status Overview'"))
    story.append(cb("Configure: Chart type: Pie or Bar"))

    add_section("8.2 Board 2 (Workgroup) Views")
    story.append(cb("Main Table View - Sort by Due Date, save as 'Main Table'"))
    story.append(cb("Timeline View - Name: 'Workgroup Timeline'"))
    story.append(cb("Calendar View - Name: 'Workgroup Calendar', Date: Workgroup Meeting Date"))
    story.append(cb("Meeting Schedule View - Filter: Show only items with meeting date set"))

    add_section("8.3 Board 3 (Draft and Review) Views")
    story.append(cb("Main Table View - Sort by Due Date, save as 'Main Table'"))
    story.append(cb("Timeline View - Name: 'Draft/Review Timeline'"))
    story.append(cb("Calendar View - Name: 'Draft/Review Calendar'"))

    add_section("8.4 Board 4 (Deliverables) Views")
    story.append(cb("Main Table View - Sort by Due Date, Group by Phase"))
    story.append(cb("Phase Progress View - Stacked Bar chart by Phase/Status"))
    story.append(cb("Timeline View - Name: 'Deliverables Timeline'"))
    story.append(cb("Dependency Map View - Name: 'Dependency Overview'"))

    add_section("8.5 Create Master Dashboard")
    story.append(cb("Navigate to Workspace -> Add -> Dashboard"))
    story.append(cb("Name: 'KDADS Policy Manual - Master Dashboard'"))

    add_subsection("Add Widgets from Board 1 (Delphi)")
    story.append(cb("Widget 1: Status overview chart"))
    story.append(cb("Widget 2: Items due this week (filtered table)"))
    story.append(cb("Widget 3: Consensus % tracker (numbers widget)"))

    add_subsection("Add Widgets from Board 2 (Workgroup)")
    story.append(cb("Widget 4: Status overview chart"))
    story.append(cb("Widget 5: Upcoming workgroup meetings (calendar widget)"))
    story.append(cb("Widget 6: Items due this week (filtered table)"))

    add_subsection("Add Widgets from Board 3 (Draft/Review)")
    story.append(cb("Widget 7: Status overview chart"))
    story.append(cb("Widget 8: Items due this week (filtered table)"))

    add_subsection("Add Widgets from Board 4 (Deliverables)")
    story.append(cb("Widget 9: Phase progress chart"))
    story.append(cb("Widget 10: Overall completion percentage"))
    story.append(cb("Widget 11: Blocked items alert"))

    add_subsection("Dashboard Filters")
    story.append(cb("Add filter: By Status (show Blocked items)"))
    story.append(cb("Add filter: By Due Date (this week/month)"))
    story.append(cb("Add filter: By Owner"))

    add_section("8.6 Views Verification Checklist")
    story.append(cb("Verify all views are created for each board"))
    story.append(cb("Test Timeline views display correctly"))
    story.append(cb("Test Calendar views show correct dates"))
    story.append(cb("Verify Dashboard widgets display data accurately"))
    story.append(cb("Test dashboard filters work as expected"))

    story.append(PageBreak())

    # ========== PHASE 9 ==========
    add_header("Phase 9: Final Validation and Testing")

    add_section("9.1 Board Structure Validation")
    add_subsection("Board 1 (Delphi)")
    story.append(cb("Confirm 4 groups exist"))
    story.append(cb("Confirm 10 status columns exist"))
    story.append(cb("Confirm 6 additional columns exist"))
    story.append(cb("Test adding a new item"))
    story.append(cb("Test updating status through all stages"))
    story.append(cb("Verify column descriptions appear on hover"))

    add_subsection("Board 2 (Workgroup)")
    story.append(cb("Confirm 9 groups exist"))
    story.append(cb("Confirm 7 status columns exist"))
    story.append(cb("Confirm 5 additional columns exist"))
    story.append(cb("Test full workflow from start to finish"))

    add_subsection("Board 3 (Draft and Review)")
    story.append(cb("Confirm placeholder groups exist"))
    story.append(cb("Confirm 6 status columns exist"))
    story.append(cb("Confirm 4 additional columns exist"))
    story.append(cb("Test full workflow"))

    add_subsection("Board 4 (Deliverables)")
    story.append(cb("Confirm 4 phase groups exist"))
    story.append(cb("Confirm all deliverable items are added"))
    story.append(cb("Test dependencies linking"))
    story.append(cb("Test progress tracking"))

    add_section("9.2 Automation Testing")
    story.append(cb("Test: Change Delphi item to 'Policy Review' -> KDADS notified?"))
    story.append(cb("Test: Change Workgroup item to 'Legal Review' -> KDADS notified?"))
    story.append(cb("Test: Set item status to 'Blocked' -> Owners notified?"))
    story.append(cb("Test: Due date reminder triggers correctly?"))
    story.append(cb("Document any automation issues"))

    add_section("9.3 Permission Testing")
    story.append(cb("Log in as ADS team member -> Verify appropriate access"))
    story.append(cb("Log in as KDADS team member -> Verify appropriate access"))
    story.append(cb("Test that users can only edit columns they own"))
    story.append(cb("Verify view-only users cannot edit"))

    add_section("9.4 Dashboard Testing")
    story.append(cb("Verify all widgets display current data"))
    story.append(cb("Test filters work correctly"))
    story.append(cb("Verify cross-board data aggregation"))
    story.append(cb("Check dashboard load time is acceptable"))

    add_section("9.5 User Acceptance Testing")
    story.append(cb("Schedule walkthrough with ADS team"))
    story.append(cb("Schedule walkthrough with KDADS team"))
    story.append(cb("Collect feedback on board organization"))
    story.append(cb("Collect feedback on column names and descriptions"))
    story.append(cb("Collect feedback on workflow stages"))
    story.append(cb("Collect feedback on automation notifications"))
    story.append(cb("Collect feedback on dashboard usefulness"))
    story.append(cb("Document requested changes"))

    add_section("9.6 Documentation and Training")
    story.append(cb("Create user guide for each board"))
    story.append(cb("Document automation logic"))
    story.append(cb("Create quick reference card for status labels"))
    story.append(cb("Schedule training session for all users"))
    story.append(cb("Set up feedback channel for ongoing improvements"))

    add_section("9.7 Go-Live Checklist")
    story.append(cb("All boards created and configured"))
    story.append(cb("All automations tested and working"))
    story.append(cb("All permissions configured correctly"))
    story.append(cb("All views and dashboard created"))
    story.append(cb("User training completed"))
    story.append(cb("Documentation delivered"))
    story.append(cb("Feedback mechanism in place"))
    story.append(cb("GO LIVE APPROVED"))

    story.append(PageBreak())

    # ========== APPENDIX A ==========
    add_header("Appendix A: Status Labels Quick Reference")

    status_ref = [
        ['Label', 'Color', 'When to Use'],
        ['Not Started', 'Gray', 'Work has not begun'],
        ['In Progress', 'Blue', 'Active work underway'],
        ['Pending Review', 'Yellow', 'Submitted, awaiting review'],
        ['Blocked', 'Red', 'Cannot proceed due to issue'],
        ['Complete', 'Green', 'Work finished'],
        ['Not Needed', 'Light Gray', 'Conditional step not required'],
        ['Scheduled', 'Purple', 'Meeting/event scheduled']
    ]

    ref_table = Table(status_ref, colWidths=[1.5*inch, 1.2*inch, 3.5*inch])
    ref_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), PRIMARY_BLUE),
        ('TEXTCOLOR', (0, 0), (-1, 0), white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
        ('TOPPADDING', (0, 0), (-1, 0), 10),
        ('BACKGROUND', (0, 1), (-1, -1), LIGHT_GRAY),
        ('GRID', (0, 0), (-1, -1), 0.5, BORDER_GRAY),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [white, LIGHT_GRAY]),
    ]))
    story.append(ref_table)

    story.append(PageBreak())

    # ========== APPENDIX B ==========
    add_header("Appendix B: Responsible Party Reference")

    add_section("Delphi Board Stages")
    delphi_data = [
        ['Stage', 'Responsible Party'],
        ['1. In-Person Kickoff', 'KDADS & ADS'],
        ['2. First Meeting - Problem ID', 'ADS'],
        ['3. Second Meeting - Solutions/Goals', 'ADS'],
        ['4. Survey Development & Iteration', 'ADS'],
        ['5. Policy Drafting', 'ADS'],
        ['6. Policy Review', 'KDADS'],
        ['7. Finalize Language', 'ADS'],
        ['8. Legal Review', 'KDADS'],
        ['9. Language Updates (if needed)', 'ADS'],
        ['10. Commissioner Sign-Off & Publish', 'KDADS']
    ]

    delphi_table = Table(delphi_data, colWidths=[3.5*inch, 2*inch])
    delphi_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), PRIMARY_BLUE),
        ('TEXTCOLOR', (0, 0), (-1, 0), white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('GRID', (0, 0), (-1, -1), 0.5, BORDER_GRAY),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [white, LIGHT_GRAY]),
    ]))
    story.append(delphi_table)
    add_space(15)

    add_section("Workgroup Board Stages")
    workgroup_data = [
        ['Stage', 'Responsible Party'],
        ['1. Initial Policy Drafting', 'ADS'],
        ['2. Policy Review', 'KDADS'],
        ['3. Workgroup Convening', 'ADS'],
        ['4. Revise & Finalize Draft', 'ADS'],
        ['5. Legal Review', 'KDADS'],
        ['6. Language Updates (if needed)', 'ADS'],
        ['7. Commissioner Sign-Off & Publish', 'KDADS']
    ]

    workgroup_table = Table(workgroup_data, colWidths=[3.5*inch, 2*inch])
    workgroup_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), PRIMARY_BLUE),
        ('TEXTCOLOR', (0, 0), (-1, 0), white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('GRID', (0, 0), (-1, -1), 0.5, BORDER_GRAY),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [white, LIGHT_GRAY]),
    ]))
    story.append(workgroup_table)
    add_space(15)

    add_section("Draft/Review Board Stages")
    draft_data = [
        ['Stage', 'Responsible Party'],
        ['1. Initial Policy Drafting', 'ADS'],
        ['2. Policy Review', 'KDADS'],
        ['3. Revise & Finalize Draft', 'ADS'],
        ['4. Legal Review', 'KDADS'],
        ['5. Language Updates (if needed)', 'ADS'],
        ['6. Commissioner Sign-Off & Publish', 'KDADS']
    ]

    draft_table = Table(draft_data, colWidths=[3.5*inch, 2*inch])
    draft_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), PRIMARY_BLUE),
        ('TEXTCOLOR', (0, 0), (-1, 0), white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('GRID', (0, 0), (-1, -1), 0.5, BORDER_GRAY),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [white, LIGHT_GRAY]),
    ]))
    story.append(draft_table)

    story.append(PageBreak())

    # ========== APPENDIX C ==========
    add_header("Appendix C: Deliverables Timeline Reference")

    timeline_data = [
        ['Phase', 'Deliverable', 'Target Date'],
        ['B', 'Initial Drafts', 'March 2026'],
        ['B', 'Workgroups Complete', 'May 2026'],
        ['B', 'Revisions Complete', 'June 2026'],
        ['B', 'Delphi Drafts Complete', 'August 2026']
    ]

    timeline_table = Table(timeline_data, colWidths=[1*inch, 3*inch, 1.5*inch])
    timeline_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), PRIMARY_BLUE),
        ('TEXTCOLOR', (0, 0), (-1, 0), white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 0.5, BORDER_GRAY),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [white, LIGHT_GRAY]),
    ]))
    story.append(timeline_table)

    story.append(PageBreak())

    # ========== APPENDIX D ==========
    add_header("Appendix D: Troubleshooting Guide")

    add_section("Issue: Automations not triggering")
    add_text("- Verify automation is turned on (toggle switch)")
    add_text("- Check trigger conditions match exactly")
    add_text("- Ensure notification recipients are board members")

    add_section("Issue: Users cannot edit items")
    add_text("- Check board permissions")
    add_text("- Verify user is assigned as Owner or Member")
    add_text("- Check column-level permissions if applicable")

    add_section("Issue: Dashboard widgets not updating")
    add_text("- Refresh dashboard")
    add_text("- Verify source board data is correct")
    add_text("- Check widget filter settings")

    add_section("Issue: Timeline view not displaying correctly")
    add_text("- Ensure Due Date column has values")
    add_text("- Check date format is correct")
    add_text("- Verify items have proper date ranges")

    add_space(30)
    story.append(Paragraph("Document Version: 1.0", styles['Note']))
    story.append(Paragraph("Created: January 2026", styles['Note']))
    story.append(Paragraph("Last Updated: [Update on each revision]", styles['Note']))

    # Build the document
    doc.build(story)
    print("PDF generated successfully: KDADS-Monday-Setup-Guide.pdf")

if __name__ == "__main__":
    build_document()
