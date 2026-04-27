
---

# 📖 README.md

```md
# Blog Management System (Secure-Software-Engineering Project)

## 📽 Demo Video
[https://drive.google.com/file/d/1pnMgMYc-M6J00gUjdSwKdqd8jtcO02HT/view?usp=drive_link]

## Overview
A small Flask web-app that mimics a blogging platform **with content moderation and role-based access control**.  
Built for a 3-person Secure-Software-Engineering course: another team will later analyze its security posture.

## System Description
* **Stack:** Flask 2, SQLite, SQLAlchemy, WTForms, Flask-Login, Flask-Limiter
* **Entities:** Users, Posts, Reports
* **Roles:** Regular User · Admin  
  RBAC enforced **server-side** (403 on illegal access).

## Major Features
1. Registration & Login with bcrypt-hashed passwords
2. Post life-cycle: draft → pending → published/remov
3. User reporting & Admin moderation
4. Rate-limited login and report routes (Flask-Limiter)
5. Seed script with demo data for instant testing

## Workflows
### 1 · Post Creation & Moderation
1. User creates post (draft) → submits for review (pending)  
2. Admin reviews pending list → publishes or removes  
3. Status change stored in DB and shown on user dashboard

### 2 · Content Reporting & Review
1. User reports an inappropriate published post  
2. Report stored in DB (open)  
3. Admin reviews report → keeps or removes post → report marked reviewed

## User Roles
| Role  | Permissions |
|-------|-------------|
| User  | CRUD own drafts, submit/pending, view published, file reports |
| Admin | View all posts, change statuses, process reports |

## Pages
1. Login/Register  
2. Dashboard (My Posts)  
3. Create/Edit Post  
4. Post Detail  
5. Admin Moderation Panel  
6. Reports Review Panel

## Running Locally
See SETUP.md for full commands.
