# KDADS Policy Manual Project – Monday.com Sequential Setup Guide

## Table of Contents
1. [Pre-Setup Preparation](#phase-0-pre-setup-preparation)
2. [Workspace Configuration](#phase-1-workspace-configuration)
3. [Board 1: Delphi Setup](#phase-2-board-1-stakeholder-engagement--delphi)
4. [Board 2: Workgroup Setup](#phase-3-board-2-stakeholder-engagement--workgroup)
5. [Board 3: Draft and Review Setup](#phase-4-board-3-stakeholder-engagement--draft-and-review)
6. [Board 4: Contract Deliverables Tracker](#phase-5-board-4-contract-deliverables-tracker)
7. [Cross-Board Configuration](#phase-6-cross-board-configuration)
8. [Automations Setup](#phase-7-automations-setup)
9. [Views and Dashboard Creation](#phase-8-views-and-dashboard-creation)
10. [Final Validation](#phase-9-final-validation-and-testing)

---

## Phase 0: Pre-Setup Preparation

### 0.1 Account & Access Verification
- [ ] Confirm Monday.com account has appropriate plan level (Pro or Enterprise recommended for automations)
- [ ] Verify admin access to create boards and workspaces
- [ ] Collect email addresses for all team members (ADS and KDADS staff)
- [ ] Determine who needs Owner vs. Member vs. Viewer access

### 0.2 Gather Required Information
- [ ] Finalize list of policy topics for Board 3 (Draft and Review) – currently TBD
- [ ] Confirm target dates for Phase A–D deliverables
- [ ] Identify primary Owner assignments for each policy topic
- [ ] Validate the 75% consensus threshold for Delphi process

### 0.3 Document Naming Conventions
- [ ] Establish naming convention for boards (e.g., "KDADS – [Board Name]")
- [ ] Establish naming convention for groups (policy topics)
- [ ] Establish color coding scheme for status labels

---

## Phase 1: Workspace Configuration

### 1.1 Create Workspace
- [ ] Navigate to Monday.com → Workspaces
- [ ] Click "Add Workspace"
- [ ] Name: **"KDADS Policy Manual Project"**
- [ ] Set workspace icon (optional – suggest policy/document icon)
- [ ] Set workspace description: "Three interconnected boards tracking policy development through Delphi, Workgroup, and Draft/Review methodologies"

### 1.2 Configure Workspace Settings
- [ ] Set workspace to "Main" or "Open" depending on visibility needs
- [ ] Add workspace members:
  - [ ] All ADS team members
  - [ ] All KDADS team members
  - [ ] Any external stakeholders who need view access

### 1.3 Create Standardized Status Labels Template
Document these labels for consistent use across all boards:
```
Status Label Colors (use consistently):
- Not Started     → Gray (#c4c4c4)
- In Progress     → Blue (#0086c0)
- Pending Review  → Yellow (#fdab3d)
- Blocked         → Red (#e2445c)
- Complete        → Green (#00c875)
```

---

## Phase 2: Board 1 – Stakeholder Engagement – Delphi

### 2.1 Create Board
- [ ] Click "Add" → "New Board"
- [ ] Select "Start from scratch"
- [ ] Name: **"Stakeholder Engagement – Delphi"**
- [ ] Set board type: Main Board
- [ ] Set board permissions: Private (ADS and KDADS only)

### 2.2 Create Groups (Policy Topics)
Create each group in this order:
- [ ] Group 1: **Provision of Direct Services**
- [ ] Group 2: **Client Eligibility**
- [ ] Group 3: **Client and Service Priority**
- [ ] Group 4: **GESN/Targeting**

For each group:
- [ ] Right-click default group → Rename
- [ ] Set group color (optional – use distinct colors for visual separation)

### 2.3 Create Process Stage Columns (Status Type)
Delete any default columns, then create in order:

| Step | Column Name | Type | Action |
|------|-------------|------|--------|
| 1 | - [ ] Create column: **"1. In-Person Kickoff"** | Status | Set labels: Not Started, In Progress, Complete |
| 2 | - [ ] Create column: **"2. First Meeting – Problem ID"** | Status | Set labels: Not Started, In Progress, Complete |
| 3 | - [ ] Create column: **"3. Second Meeting – Solutions/Goals"** | Status | Set labels: Not Started, In Progress, Complete |
| 4 | - [ ] Create column: **"4. Survey Development & Iteration"** | Status | Set labels: Not Started, In Progress, Pending Review, Complete |
| 5 | - [ ] Create column: **"5. Policy Drafting"** | Status | Set labels: Not Started, In Progress, Complete |
| 6 | - [ ] Create column: **"6. Policy Review"** | Status | Set labels: Not Started, In Progress, Pending Review, Complete |
| 7 | - [ ] Create column: **"7. Finalize Language"** | Status | Set labels: Not Started, In Progress, Complete |
| 8 | - [ ] Create column: **"8. Legal Review"** | Status | Set labels: Not Started, In Progress, Pending Review, Blocked, Complete |
| 9 | - [ ] Create column: **"9. Language Updates (if needed)"** | Status | Set labels: Not Needed, Not Started, In Progress, Complete |
| 10 | - [ ] Create column: **"10. Commissioner Sign-Off & Publish"** | Status | Set labels: Not Started, In Progress, Complete |

### 2.4 Create Additional Columns
| Step | Column Name | Type | Configuration |
|------|-------------|------|---------------|
| 1 | - [ ] Create column: **"Owner"** | People | Allow multiple people |
| 2 | - [ ] Create column: **"Due Date"** | Date | Enable deadline mode |
| 3 | - [ ] Create column: **"Survey Round #"** | Numbers | Set unit: none, allow decimals: no |
| 4 | - [ ] Create column: **"Consensus %"** | Numbers | Set unit: %, range 0-100 |
| 5 | - [ ] Create column: **"Notes/Blockers"** | Long Text | Enable rich text formatting |
| 6 | - [ ] Create column: **"Responsible Party"** | Dropdown | Options: ADS, KDADS, Both |

### 2.5 Add Items (Placeholder Rows)
For each group, add at least one item/row:
- [ ] In "Provision of Direct Services" → Add item: "Policy Development Item 1"
- [ ] In "Client Eligibility" → Add item: "Policy Development Item 1"
- [ ] In "Client and Service Priority" → Add item: "Policy Development Item 1"
- [ ] In "GESN/Targeting" → Add item: "Policy Development Item 1"

### 2.6 Set Column Descriptions
Right-click each column header → "Column Description":
- [ ] "1. In-Person Kickoff" → "Establish Delphi group (KDADS & ADS)"
- [ ] "2. First Meeting – Problem ID" → "Identify policy problem areas (ADS)"
- [ ] "3. Second Meeting – Solutions/Goals" → "Establish potential solutions (ADS)"
- [ ] "4. Survey Development & Iteration" → "Iterate until 75% consensus (ADS)"
- [ ] "5. Policy Drafting" → "Draft policy language (ADS)"
- [ ] "6. Policy Review" → "KDADS review of draft"
- [ ] "7. Finalize Language" → "Finalize policy language (ADS)"
- [ ] "8. Legal Review" → "Legal review (KDADS)"
- [ ] "9. Language Updates (if needed)" → "Conditional on legal feedback (ADS)"
- [ ] "10. Commissioner Sign-Off & Publish" → "Terminal stage (KDADS)"

### 2.7 Board 1 Verification Checklist
- [ ] Verify all 4 groups are created
- [ ] Verify all 10 status columns exist
- [ ] Verify all 6 additional columns exist
- [ ] Verify column descriptions are set
- [ ] Test adding/editing an item

---

## Phase 3: Board 2 – Stakeholder Engagement – Workgroup

### 3.1 Create Board
- [ ] Click "Add" → "New Board"
- [ ] Select "Start from scratch"
- [ ] Name: **"Stakeholder Engagement – Workgroup"**
- [ ] Set board type: Main Board
- [ ] Set board permissions: Private (ADS and KDADS only)

### 3.2 Create Groups (Policy Topics)
Create each group in this order:
- [ ] Group 1: **Area Plans on Aging**
- [ ] Group 2: **AAA Advisory Council**
- [ ] Group 3: **Conflicts of Interest**
- [ ] Group 4: **Title III/VI Coordination**
- [ ] Group 5: **Congregate Nutrition Services**
- [ ] Group 6: **Home Delivered Meals**
- [ ] Group 7: **Grab & Go Nutrition Services**
- [ ] Group 8: **Monitoring**
- [ ] Group 9: **NSIP**

For each group:
- [ ] Right-click default group → Rename
- [ ] Set group color (optional)

### 3.3 Create Process Stage Columns (Status Type)
Delete any default columns, then create in order:

| Step | Column Name | Type | Action |
|------|-------------|------|--------|
| 1 | - [ ] Create column: **"1. Initial Policy Drafting"** | Status | Set labels: Not Started, In Progress, Complete |
| 2 | - [ ] Create column: **"2. Policy Review"** | Status | Set labels: Not Started, In Progress, Pending Review, Complete |
| 3 | - [ ] Create column: **"3. Workgroup Convening"** | Status | Set labels: Not Started, Scheduled, In Progress, Complete |
| 4 | - [ ] Create column: **"4. Revise & Finalize Draft"** | Status | Set labels: Not Started, In Progress, Complete |
| 5 | - [ ] Create column: **"5. Legal Review"** | Status | Set labels: Not Started, In Progress, Pending Review, Blocked, Complete |
| 6 | - [ ] Create column: **"6. Language Updates (if needed)"** | Status | Set labels: Not Needed, Not Started, In Progress, Complete |
| 7 | - [ ] Create column: **"7. Commissioner Sign-Off & Publish"** | Status | Set labels: Not Started, In Progress, Complete |

### 3.4 Create Additional Columns
| Step | Column Name | Type | Configuration |
|------|-------------|------|---------------|
| 1 | - [ ] Create column: **"Owner"** | People | Allow multiple people |
| 2 | - [ ] Create column: **"Due Date"** | Date | Enable deadline mode |
| 3 | - [ ] Create column: **"Workgroup Meeting Date"** | Date | Standard date picker |
| 4 | - [ ] Create column: **"Notes/Blockers"** | Long Text | Enable rich text formatting |
| 5 | - [ ] Create column: **"Responsible Party"** | Dropdown | Options: ADS, KDADS, Both |

### 3.5 Add Items (Placeholder Rows)
For each group, add at least one item/row:
- [ ] In "Area Plans on Aging" → Add item: "Policy Development Item 1"
- [ ] In "AAA Advisory Council" → Add item: "Policy Development Item 1"
- [ ] In "Conflicts of Interest" → Add item: "Policy Development Item 1"
- [ ] In "Title III/VI Coordination" → Add item: "Policy Development Item 1"
- [ ] In "Congregate Nutrition Services" → Add item: "Policy Development Item 1"
- [ ] In "Home Delivered Meals" → Add item: "Policy Development Item 1"
- [ ] In "Grab & Go Nutrition Services" → Add item: "Policy Development Item 1"
- [ ] In "Monitoring" → Add item: "Policy Development Item 1"
- [ ] In "NSIP" → Add item: "Policy Development Item 1"

### 3.6 Set Column Descriptions
Right-click each column header → "Column Description":
- [ ] "1. Initial Policy Drafting" → "Initial draft creation (ADS)"
- [ ] "2. Policy Review" → "KDADS review of initial draft"
- [ ] "3. Workgroup Convening" → "Convene workgroup for collaborative review (ADS)"
- [ ] "4. Revise & Finalize Draft" → "Incorporate workgroup feedback (ADS)"
- [ ] "5. Legal Review" → "Legal review (KDADS)"
- [ ] "6. Language Updates (if needed)" → "Conditional on legal feedback (ADS)"
- [ ] "7. Commissioner Sign-Off & Publish" → "Terminal stage (KDADS)"

### 3.7 Board 2 Verification Checklist
- [ ] Verify all 9 groups are created
- [ ] Verify all 7 status columns exist
- [ ] Verify all 5 additional columns exist
- [ ] Verify column descriptions are set
- [ ] Test adding/editing an item

---

## Phase 4: Board 3 – Stakeholder Engagement – Draft and Review

### 4.1 Create Board
- [ ] Click "Add" → "New Board"
- [ ] Select "Start from scratch"
- [ ] Name: **"Stakeholder Engagement – Draft and Review"**
- [ ] Set board type: Main Board
- [ ] Set board permissions: Private (ADS and KDADS only)

### 4.2 Create Groups (Policy Topics)
**Note: Policy topics are TBD – create placeholder groups:**
- [ ] Group 1: **TBD Policy Topic 1**
- [ ] Group 2: **TBD Policy Topic 2**
- [ ] Group 3: **TBD Policy Topic 3**

*Update these groups once policy topics are finalized*

### 4.3 Create Process Stage Columns (Status Type)
Delete any default columns, then create in order:

| Step | Column Name | Type | Action |
|------|-------------|------|--------|
| 1 | - [ ] Create column: **"1. Initial Policy Drafting"** | Status | Set labels: Not Started, In Progress, Complete |
| 2 | - [ ] Create column: **"2. Policy Review"** | Status | Set labels: Not Started, In Progress, Pending Review, Complete |
| 3 | - [ ] Create column: **"3. Revise & Finalize Draft"** | Status | Set labels: Not Started, In Progress, Complete |
| 4 | - [ ] Create column: **"4. Legal Review"** | Status | Set labels: Not Started, In Progress, Pending Review, Blocked, Complete |
| 5 | - [ ] Create column: **"5. Language Updates (if needed)"** | Status | Set labels: Not Needed, Not Started, In Progress, Complete |
| 6 | - [ ] Create column: **"6. Commissioner Sign-Off & Publish"** | Status | Set labels: Not Started, In Progress, Complete |

### 4.4 Create Additional Columns
| Step | Column Name | Type | Configuration |
|------|-------------|------|---------------|
| 1 | - [ ] Create column: **"Owner"** | People | Allow multiple people |
| 2 | - [ ] Create column: **"Due Date"** | Date | Enable deadline mode |
| 3 | - [ ] Create column: **"Notes/Blockers"** | Long Text | Enable rich text formatting |
| 4 | - [ ] Create column: **"Responsible Party"** | Dropdown | Options: ADS, KDADS, Both |

### 4.5 Add Items (Placeholder Rows)
- [ ] In each TBD group → Add item: "Policy Development Item 1"

### 4.6 Set Column Descriptions
Right-click each column header → "Column Description":
- [ ] "1. Initial Policy Drafting" → "Initial draft creation (ADS)"
- [ ] "2. Policy Review" → "KDADS review of initial draft"
- [ ] "3. Revise & Finalize Draft" → "Finalize draft based on review (ADS)"
- [ ] "4. Legal Review" → "Legal review (KDADS)"
- [ ] "5. Language Updates (if needed)" → "Conditional on legal feedback (ADS)"
- [ ] "6. Commissioner Sign-Off & Publish" → "Terminal stage (KDADS)"

### 4.7 Board 3 Verification Checklist
- [ ] Verify placeholder groups are created
- [ ] Verify all 6 status columns exist
- [ ] Verify all 4 additional columns exist
- [ ] Verify column descriptions are set
- [ ] Test adding/editing an item
- [ ] **ACTION REQUIRED**: Update groups when policy topics are finalized

---

## Phase 5: Board 4 – Contract Deliverables Tracker

### 5.1 Create Board
- [ ] Click "Add" → "New Board"
- [ ] Select "Start from scratch"
- [ ] Name: **"Contract Deliverables Tracker"**
- [ ] Set board type: Main Board
- [ ] Set board permissions: Private (ADS and KDADS only)

### 5.2 Create Groups (Contract Phases)
Create each group in this order:
- [ ] Group 1: **Phase A – New Policy & Procedures Manual**
- [ ] Group 2: **Phase B – Stakeholder Engagement**
- [ ] Group 3: **Phase C – Final Manual Assembly**
- [ ] Group 4: **Phase D – Training & Implementation**

For each group:
- [ ] Right-click default group → Rename
- [ ] Set group color:
  - Phase A → Blue
  - Phase B → Purple
  - Phase C → Orange
  - Phase D → Green

### 5.3 Create Columns
| Step | Column Name | Type | Configuration |
|------|-------------|------|---------------|
| 1 | - [ ] Create column: **"Deliverable"** | Text | Standard text |
| 2 | - [ ] Create column: **"Phase"** | Dropdown | Options: A, B, C, D |
| 3 | - [ ] Create column: **"Status"** | Status | Labels: Not Started, In Progress, Pending Review, Blocked, Complete |
| 4 | - [ ] Create column: **"Due Date"** | Date | Enable deadline mode |
| 5 | - [ ] Create column: **"Owner"** | People | Allow multiple people |
| 6 | - [ ] Create column: **"Dependencies"** | Link to Item | Link to items in this board and other boards |
| 7 | - [ ] Create column: **"Completion %"** | Progress Tracking | Or use Numbers column with % unit |
| 8 | - [ ] Create column: **"Key Milestones"** | Long Text | Enable rich text formatting |
| 9 | - [ ] Create column: **"Notes"** | Long Text | Enable rich text formatting |

### 5.4 Add Deliverable Items

#### Phase A Items:
- [ ] Add item: **"New Policy & Procedures Manual"**
  - Key Milestones: "All finalized OAA policies; structured for future program expansion"
- [ ] Add item: **"Project Management Hub"**
  - Key Milestones: "Policy inventory (update/remove/replace); change tracking mechanism"

#### Phase B Items:
- [ ] Add item: **"Initial Drafts Completion"**
  - Due Date: March 2026
- [ ] Add item: **"Workgroups Complete"**
  - Due Date: May 2026
- [ ] Add item: **"Revisions Complete"**
  - Due Date: June 2026
- [ ] Add item: **"Delphi Drafts Complete"**
  - Due Date: August 2026

#### Phase C Items:
- [ ] Add item: **"Legal/Leadership Revisions"**
- [ ] Add item: **"Dependency Mapping"**
- [ ] Add item: **"Anchor Policy Identification"**

#### Phase D Items:
- [ ] Add item: **"Workgroup Discussions (3)"**
- [ ] Add item: **"Forms & Job Aids Development"**
- [ ] Add item: **"In-Person Training (1)"**
- [ ] Add item: **"Webinar (1)"**
- [ ] Add item: **"E-Learning Modules"**

### 5.5 Configure Dependencies
- [ ] Link Phase B items to relevant policy boards
- [ ] Link Phase C items to Phase B completion
- [ ] Link Phase D items to Phase C completion

### 5.6 Board 4 Verification Checklist
- [ ] Verify all 4 phase groups are created
- [ ] Verify all 9 columns exist
- [ ] Verify all deliverable items are added
- [ ] Verify dependencies are linked
- [ ] Test progress tracking functionality

---

## Phase 6: Cross-Board Configuration

### 6.1 Standardize Status Labels Across All Boards
For each board, verify status columns use these consistent labels:

| Label | Color Code | Usage |
|-------|------------|-------|
| - [ ] Not Started | Gray (#c4c4c4) | Default state |
| - [ ] In Progress | Blue (#0086c0) | Active work |
| - [ ] Pending Review | Yellow (#fdab3d) | Awaiting review |
| - [ ] Blocked | Red (#e2445c) | Cannot proceed |
| - [ ] Complete | Green (#00c875) | Finished |
| - [ ] Not Needed | Light Gray (#c4c4c4) | For conditional steps |
| - [ ] Scheduled | Purple (#a25ddc) | For meetings/events |

### 6.2 Configure Board Permissions

#### Board 1 (Delphi):
- [ ] Set ADS team members as Owners for columns 2, 3, 4, 5, 7, 9
- [ ] Set KDADS team members as Owners for columns 1, 6, 8, 10

#### Board 2 (Workgroup):
- [ ] Set ADS team members as Owners for columns 1, 3, 4, 6
- [ ] Set KDADS team members as Owners for columns 2, 5, 7

#### Board 3 (Draft and Review):
- [ ] Set ADS team members as Owners for columns 1, 3, 5
- [ ] Set KDADS team members as Owners for columns 2, 4, 6

#### Board 4 (Deliverables):
- [ ] Set both ADS and KDADS as board Owners

### 6.3 Create Board Connections
- [ ] Connect Board 4 (Deliverables) to Board 1 (Delphi) via Dependencies column
- [ ] Connect Board 4 (Deliverables) to Board 2 (Workgroup) via Dependencies column
- [ ] Connect Board 4 (Deliverables) to Board 3 (Draft/Review) via Dependencies column

### 6.4 Cross-Board Verification
- [ ] Verify all boards appear in workspace
- [ ] Verify all team members have appropriate access
- [ ] Test board connections/links

---

## Phase 7: Automations Setup

### 7.1 Board 1 (Delphi) Automations

#### Automation 1: Notify KDADS on Policy Review
- [ ] Navigate to Board 1 → Automations → Add Automation
- [ ] Trigger: When "6. Policy Review" changes to "In Progress"
- [ ] Action: Notify KDADS team members
- [ ] Message: "Policy item ready for KDADS review in Delphi board"

#### Automation 2: Notify KDADS on Legal Review
- [ ] Trigger: When "8. Legal Review" changes to "In Progress"
- [ ] Action: Notify KDADS team members
- [ ] Message: "Policy item ready for Legal Review in Delphi board"

#### Automation 3: Notify ADS on Language Updates Needed
- [ ] Trigger: When "9. Language Updates (if needed)" changes to "Not Started"
- [ ] Action: Notify ADS team members
- [ ] Message: "Language updates required based on legal feedback"

#### Automation 4: Due Date Reminder
- [ ] Trigger: When Due Date arrives
- [ ] Action: Notify Owner
- [ ] Message: "Due date reached for Delphi policy item"

#### Automation 5: Approaching Deadline Warning
- [ ] Trigger: 3 days before Due Date
- [ ] Action: Notify Owner
- [ ] Message: "Delphi policy item due in 3 days"

### 7.2 Board 2 (Workgroup) Automations

#### Automation 1: Notify KDADS on Policy Review
- [ ] Navigate to Board 2 → Automations → Add Automation
- [ ] Trigger: When "2. Policy Review" changes to "In Progress"
- [ ] Action: Notify KDADS team members
- [ ] Message: "Policy item ready for KDADS review in Workgroup board"

#### Automation 2: Notify KDADS on Legal Review
- [ ] Trigger: When "5. Legal Review" changes to "In Progress"
- [ ] Action: Notify KDADS team members
- [ ] Message: "Policy item ready for Legal Review in Workgroup board"

#### Automation 3: Notify ADS on Language Updates Needed
- [ ] Trigger: When "6. Language Updates (if needed)" changes to "Not Started"
- [ ] Action: Notify ADS team members
- [ ] Message: "Language updates required based on legal feedback"

#### Automation 4: Workgroup Meeting Reminder
- [ ] Trigger: 1 day before Workgroup Meeting Date
- [ ] Action: Notify Owner
- [ ] Message: "Workgroup meeting scheduled for tomorrow"

#### Automation 5: Due Date Reminder
- [ ] Trigger: When Due Date arrives
- [ ] Action: Notify Owner

### 7.3 Board 3 (Draft and Review) Automations

#### Automation 1: Notify KDADS on Policy Review
- [ ] Navigate to Board 3 → Automations → Add Automation
- [ ] Trigger: When "2. Policy Review" changes to "In Progress"
- [ ] Action: Notify KDADS team members
- [ ] Message: "Policy item ready for KDADS review in Draft/Review board"

#### Automation 2: Notify KDADS on Legal Review
- [ ] Trigger: When "4. Legal Review" changes to "In Progress"
- [ ] Action: Notify KDADS team members
- [ ] Message: "Policy item ready for Legal Review in Draft/Review board"

#### Automation 3: Notify ADS on Language Updates Needed
- [ ] Trigger: When "5. Language Updates (if needed)" changes to "Not Started"
- [ ] Action: Notify ADS team members
- [ ] Message: "Language updates required based on legal feedback"

#### Automation 4: Due Date Reminder
- [ ] Trigger: When Due Date arrives
- [ ] Action: Notify Owner

### 7.4 Board 4 (Deliverables) Automations

#### Automation 1: Phase Completion Notification
- [ ] Trigger: When all items in a group have Status = "Complete"
- [ ] Action: Notify all board members
- [ ] Message: "Phase [group name] completed!"

#### Automation 2: Blocked Item Alert
- [ ] Trigger: When Status changes to "Blocked"
- [ ] Action: Notify all Owners
- [ ] Message: "Deliverable item is blocked - attention required"

#### Automation 3: Due Date Warning
- [ ] Trigger: 7 days before Due Date
- [ ] Action: Notify Owner
- [ ] Message: "Deliverable due in 7 days"

### 7.5 Automation Verification Checklist
- [ ] Test each automation by changing status values
- [ ] Verify notifications are received by correct team members
- [ ] Confirm automation triggers work as expected
- [ ] Document any automation failures or issues

---

## Phase 8: Views and Dashboard Creation

### 8.1 Board 1 (Delphi) Views

#### Main Table View (Default)
- [ ] Verify default table view shows all columns
- [ ] Sort by Due Date (ascending)
- [ ] Save view as "Main Table"

#### Timeline/Gantt View
- [ ] Click "Add View" → "Timeline"
- [ ] Name: "Delphi Timeline"
- [ ] Configure:
  - [ ] Date column: Due Date
  - [ ] Group by: Policy Topic (groups)
  - [ ] Color by: Status of final column

#### Calendar View
- [ ] Click "Add View" → "Calendar"
- [ ] Name: "Delphi Calendar"
- [ ] Configure:
  - [ ] Date column: Due Date
  - [ ] Show item name and status

#### Status Overview (Chart)
- [ ] Click "Add View" → "Chart"
- [ ] Name: "Status Overview"
- [ ] Configure:
  - [ ] Chart type: Pie or Bar
  - [ ] Group by: Latest status column

### 8.2 Board 2 (Workgroup) Views

#### Main Table View (Default)
- [ ] Verify default table view shows all columns
- [ ] Sort by Due Date (ascending)
- [ ] Save view as "Main Table"

#### Timeline/Gantt View
- [ ] Click "Add View" → "Timeline"
- [ ] Name: "Workgroup Timeline"
- [ ] Configure:
  - [ ] Date column: Due Date
  - [ ] Group by: Policy Topic (groups)

#### Calendar View
- [ ] Click "Add View" → "Calendar"
- [ ] Name: "Workgroup Calendar"
- [ ] Configure:
  - [ ] Date column: Workgroup Meeting Date
  - [ ] Show item name

#### Workgroup Meeting Schedule
- [ ] Click "Add View" → "Calendar"
- [ ] Name: "Meeting Schedule"
- [ ] Filter: Show only items with Workgroup Meeting Date set

### 8.3 Board 3 (Draft and Review) Views

#### Main Table View (Default)
- [ ] Verify default table view shows all columns
- [ ] Sort by Due Date (ascending)
- [ ] Save view as "Main Table"

#### Timeline/Gantt View
- [ ] Click "Add View" → "Timeline"
- [ ] Name: "Draft/Review Timeline"
- [ ] Configure date and grouping

#### Calendar View
- [ ] Click "Add View" → "Calendar"
- [ ] Name: "Draft/Review Calendar"

### 8.4 Board 4 (Deliverables) Views

#### Main Table View (Default)
- [ ] Sort by Due Date (ascending)
- [ ] Group by Phase

#### Phase Progress View
- [ ] Click "Add View" → "Chart"
- [ ] Name: "Phase Progress"
- [ ] Configure:
  - [ ] Chart type: Stacked Bar
  - [ ] Group by: Phase
  - [ ] Stack by: Status

#### Timeline/Gantt View
- [ ] Click "Add View" → "Timeline"
- [ ] Name: "Deliverables Timeline"
- [ ] Configure:
  - [ ] Date column: Due Date
  - [ ] Group by: Phase

#### Dependency Map View
- [ ] Click "Add View" → "Workload" or use "Files" view
- [ ] Name: "Dependency Overview"

### 8.5 Create Master Dashboard

#### Dashboard Setup
- [ ] Navigate to Workspace → Add → Dashboard
- [ ] Name: **"KDADS Policy Manual – Master Dashboard"**

#### Add Widgets from Board 1 (Delphi)
- [ ] Widget 1: Status overview chart
- [ ] Widget 2: Items due this week (filtered table)
- [ ] Widget 3: Consensus % tracker (numbers widget)

#### Add Widgets from Board 2 (Workgroup)
- [ ] Widget 4: Status overview chart
- [ ] Widget 5: Upcoming workgroup meetings (calendar widget)
- [ ] Widget 6: Items due this week (filtered table)

#### Add Widgets from Board 3 (Draft/Review)
- [ ] Widget 7: Status overview chart
- [ ] Widget 8: Items due this week (filtered table)

#### Add Widgets from Board 4 (Deliverables)
- [ ] Widget 9: Phase progress chart
- [ ] Widget 10: Overall completion percentage
- [ ] Widget 11: Blocked items alert

#### Dashboard Filters
- [ ] Add filter: By Status (show Blocked items)
- [ ] Add filter: By Due Date (this week/month)
- [ ] Add filter: By Owner

### 8.6 Views Verification Checklist
- [ ] Verify all views are created for each board
- [ ] Test Timeline views display correctly
- [ ] Test Calendar views show correct dates
- [ ] Verify Dashboard widgets display data accurately
- [ ] Test dashboard filters work as expected

---

## Phase 9: Final Validation and Testing

### 9.1 Board Structure Validation

#### Board 1 (Delphi)
- [ ] Confirm 4 groups exist
- [ ] Confirm 10 status columns exist
- [ ] Confirm 6 additional columns exist
- [ ] Test adding a new item
- [ ] Test updating status through all stages
- [ ] Verify column descriptions appear on hover

#### Board 2 (Workgroup)
- [ ] Confirm 9 groups exist
- [ ] Confirm 7 status columns exist
- [ ] Confirm 5 additional columns exist
- [ ] Test full workflow from start to finish

#### Board 3 (Draft and Review)
- [ ] Confirm placeholder groups exist
- [ ] Confirm 6 status columns exist
- [ ] Confirm 4 additional columns exist
- [ ] Test full workflow

#### Board 4 (Deliverables)
- [ ] Confirm 4 phase groups exist
- [ ] Confirm all deliverable items are added
- [ ] Test dependencies linking
- [ ] Test progress tracking

### 9.2 Automation Testing

- [ ] Test: Change Delphi item to "Policy Review" → KDADS notified?
- [ ] Test: Change Workgroup item to "Legal Review" → KDADS notified?
- [ ] Test: Set item status to "Blocked" → Owners notified?
- [ ] Test: Due date reminder triggers correctly?
- [ ] Document any automation issues

### 9.3 Permission Testing

- [ ] Log in as ADS team member → Verify appropriate access
- [ ] Log in as KDADS team member → Verify appropriate access
- [ ] Test that users can only edit columns they own
- [ ] Verify view-only users cannot edit

### 9.4 Dashboard Testing

- [ ] Verify all widgets display current data
- [ ] Test filters work correctly
- [ ] Verify cross-board data aggregation
- [ ] Check dashboard load time is acceptable

### 9.5 User Acceptance Testing

- [ ] Schedule walkthrough with ADS team
- [ ] Schedule walkthrough with KDADS team
- [ ] Collect feedback on:
  - [ ] Board organization
  - [ ] Column names and descriptions
  - [ ] Workflow stages
  - [ ] Automation notifications
  - [ ] Dashboard usefulness
- [ ] Document requested changes

### 9.6 Documentation and Training

- [ ] Create user guide for each board
- [ ] Document automation logic
- [ ] Create quick reference card for status labels
- [ ] Schedule training session for all users
- [ ] Set up feedback channel for ongoing improvements

### 9.7 Go-Live Checklist

- [ ] All boards created and configured
- [ ] All automations tested and working
- [ ] All permissions configured correctly
- [ ] All views and dashboard created
- [ ] User training completed
- [ ] Documentation delivered
- [ ] Feedback mechanism in place
- [ ] **GO LIVE APPROVED**

---

## Appendix A: Quick Reference – Status Labels

| Label | Color | When to Use |
|-------|-------|-------------|
| Not Started | Gray | Work has not begun |
| In Progress | Blue | Active work underway |
| Pending Review | Yellow | Submitted, awaiting review |
| Blocked | Red | Cannot proceed due to issue |
| Complete | Green | Work finished |
| Not Needed | Light Gray | Conditional step not required |
| Scheduled | Purple | Meeting/event scheduled |

---

## Appendix B: Responsible Party Reference

### Delphi Board Stages
| Stage | Responsible Party |
|-------|-------------------|
| 1. In-Person Kickoff | KDADS & ADS |
| 2. First Meeting – Problem ID | ADS |
| 3. Second Meeting – Solutions/Goals | ADS |
| 4. Survey Development & Iteration | ADS |
| 5. Policy Drafting | ADS |
| 6. Policy Review | KDADS |
| 7. Finalize Language | ADS |
| 8. Legal Review | KDADS |
| 9. Language Updates (if needed) | ADS |
| 10. Commissioner Sign-Off & Publish | KDADS |

### Workgroup Board Stages
| Stage | Responsible Party |
|-------|-------------------|
| 1. Initial Policy Drafting | ADS |
| 2. Policy Review | KDADS |
| 3. Workgroup Convening | ADS |
| 4. Revise & Finalize Draft | ADS |
| 5. Legal Review | KDADS |
| 6. Language Updates (if needed) | ADS |
| 7. Commissioner Sign-Off & Publish | KDADS |

### Draft/Review Board Stages
| Stage | Responsible Party |
|-------|-------------------|
| 1. Initial Policy Drafting | ADS |
| 2. Policy Review | KDADS |
| 3. Revise & Finalize Draft | ADS |
| 4. Legal Review | KDADS |
| 5. Language Updates (if needed) | ADS |
| 6. Commissioner Sign-Off & Publish | KDADS |

---

## Appendix C: Deliverables Timeline Reference

| Phase | Deliverable | Target Date |
|-------|-------------|-------------|
| B | Initial Drafts | March 2026 |
| B | Workgroups Complete | May 2026 |
| B | Revisions Complete | June 2026 |
| B | Delphi Drafts Complete | August 2026 |

---

## Appendix D: Troubleshooting Guide

### Common Issues

**Issue: Automations not triggering**
- Verify automation is turned on (toggle switch)
- Check trigger conditions match exactly
- Ensure notification recipients are board members

**Issue: Users cannot edit items**
- Check board permissions
- Verify user is assigned as Owner or Member
- Check column-level permissions if applicable

**Issue: Dashboard widgets not updating**
- Refresh dashboard
- Verify source board data is correct
- Check widget filter settings

**Issue: Timeline view not displaying correctly**
- Ensure Due Date column has values
- Check date format is correct
- Verify items have proper date ranges

---

*Document Version: 1.0*
*Created: January 2026*
*Last Updated: [Update on each revision]*
