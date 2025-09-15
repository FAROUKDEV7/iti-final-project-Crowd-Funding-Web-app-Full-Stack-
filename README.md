A full-stack crowdfunding platform built with Django that enables Egyptian creators to fund their projects through community support. FundEgypt provides a complete solution for project creators to launch campaigns and for supporters to discover and back innovative ideas.



✨ Features
🔐 Authentication System
User registration with email verification

Secure login/logout functionality

Password reset via email

Profile management with avatar uploads

Social authentication support

💼 Project Management
Create and manage fundraising campaigns

Project categorization system

Multiple image uploads with preview

Tagging system for better discovery

Funding goals with progress tracking


Donation history and receipts

Real-time funding updates

Support for multiple payment methods

💬 Community Features
Comment system with replies

Project rating and reviews

Social sharing integration

Email notifications for updates

👨‍💻 Admin Dashboard
User management system

Project moderation tools

Category management

Financial reporting

🏗️ Technology Stack
Backend
Django - High-level Python web framework

Frontend
HTML5 - Semantic markup

CSS3 - Modern styling with Flexbox/Grid

JavaScript (ES6) - Interactive functionality

Font Awesome - Icon library

Email service (SendGrid/Mailgun)

Cloud storage (AWS S3/Cloudinary)

SMS services for Egyptian numbers

🗄️ Database Schema
The application uses a relational database design with these key models:

User - Extended Django user model with profile information

Project - Campaign details, goals, and timelines

Category - Project categorization system

Donation - Transaction records and payment information

Comment - User engagement and discussions

Image - Project media management

Tag - Project tagging for discovery

Test coverage includes:

Model validation tests

View and form tests

Authentication tests
