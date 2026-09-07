# Society Hub: Secure Society Management Platform

## Overview: -
Society Hub is a full-stack, role-based management application designed to centralize residential community operations. Built to replace chaotic informal communication (like WhatsApp groups), this platform enforces strict standard operating procedures (SOPs) for visitor access, maintenance tracking, and emergency response **inspired by the military housing rules**. 

This prototype was developed for a hackathon, prioritizing operational discipline and structured database management over simple vanity features.

## Key Features: -
* Role-Based Access Control (RBAC): Secure, distinct operational environments for the Secretary (Admin), Gate Security, and standard Residents.
* Strict Gate Security Protocol: A specialized terminal for security guards to digitally log visitors, enforcing a mandatory verbal phone verification SOP prior to granting access.
* Helpdesk Ticketing System: A complete CRUD database ledger allowing residents to report maintenance issues and the management committee to track and resolve them.
* Asynchronous Emergency Alerts: JavaScript-powered SOS triggers (Fire, Medical, Earthquake) that dispatch immediate JSON payloads to the central server without reloading the page.
* Live Notice Board: Dynamic, database-driven community announcements.

## Technology Stack: -
* Frontend: HTML5, CSS3 (CSS Grid), Vanilla JavaScript (Fetch API)
* Backend: Python 3, Flask (Micro Web-Framework)
* Database: SQLite3 (Relational Database)

## How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/kranurag4321-dev/Society-Hub.git](https://github.com/kranurag4321-dev/Society-Hub.git)

##Default Test Credentials
    Use these accounts to test the Role-Based Access Control system:
    
      ( Admin           secret123)
       (Gate Security   guard123)
             ( Flat 101       resident123)
