# InterviewGPT AI -- Intelligent Interview Preparation Platform

## Requirement Gathering

### Problem Statement

Job seekers often prepare using generic resources that do not align with
their resume or target job description. Recruiters also spend
significant time conducting repetitive screening interviews. This
platform uses AI to personalize interview preparation and automate
technical assessments.

### Stakeholders

-   Job Seekers
-   Software Engineers
-   Data Scientists
-   Students
-   Recruiters
-   Hiring Managers
-   Admin

## Functional Requirements

### Authentication

-   User registration/login
-   Google OAuth
-   Email verification
-   Forgot/reset password
-   JWT + Refresh Tokens

### User Profile

-   Update profile
-   Education
-   Experience
-   Certifications
-   Preferred technologies

### Resume Management

-   Upload PDF/DOCX
-   Resume parsing
-   SHA-256 duplicate detection
-   Version management
-   Delete/download resume
-   Extract skills, projects, education, certifications

### Job Description Analyzer

-   Upload PDF/DOCX/Text
-   Extract required skills
-   ATS score
-   Skill gap analysis
-   Missing keywords

### Resume Improvement

-   ATS optimization
-   Grammar suggestions
-   Better project descriptions
-   Improved summary

### AI Interview Generator

-   Technology selection
-   Difficulty selection
-   Technical, coding, behavioral and scenario questions

### Interview Session

-   Timer
-   Save progress
-   Resume interview
-   Skip question
-   End interview

### Answer Evaluation

-   Technical correctness
-   Completeness
-   Communication
-   Suggestions
-   Overall score

### Progress Dashboard

-   Interview history
-   Technology-wise score
-   Weak areas
-   Strong areas
-   Progress trends

### Admin

-   User management
-   Analytics
-   Prompt management
-   API usage
-   Logs

## Non-Functional Requirements

-   AI response \< 10 seconds
-   Search latency \< 500 ms
-   99.9% availability
-   Horizontal scalability
-   JWT security
-   HTTPS
-   RBAC
-   Redis caching
-   Celery background workers
-   Prometheus & Grafana monitoring
-   Structured logging
-   Retry mechanisms
-   Clean Architecture
-   Repository Pattern
-   Unit & Integration Tests

## High Level Design

``` text
React Frontend
      |
FastAPI Backend
      |
+-------------------------------+
| Auth | Resume | Interview API |
+-------------------------------+
             |
      AI Orchestrator
             |
+-------------------------------+
| PostgreSQL | Qdrant | Redis   |
| Celery     | LLM API          |
+-------------------------------+
```

## Low Level Design

``` text
backend/
 ├── api/
 ├── models/
 ├── schemas/
 ├── services/
 ├── repositories/
 ├── workers/
 ├── prompts/
 ├── utils/
 ├── db/
 ├── core/
 └── tests/
```

### Design Decisions

-   Modular Monolith architecture
-   Async resume parsing with Celery
-   RAG for interview generation and evaluation
-   SHA-256 resume deduplication
-   Service + Repository layers
-   PostgreSQL for transactional data
-   Qdrant for semantic search
-   Redis for cache and task queue
