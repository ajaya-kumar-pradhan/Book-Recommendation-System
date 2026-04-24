Kindle Book Recommendation Engine
�
￼ ￼ ￼ 


📌 Overview
Book Recommendation system is a production-grade collaborative filtering recommendation system built on 520,000+ Amazon Kindle ratings. It mirrors the personalisation architecture used by platforms like Amazon, Netflix, and Spotify — surfacing relevant book recommendations in under 2 seconds, with a 95.76% Recall@10.
Deployed 24/7 on Hugging Face Spaces with a live, interactive Streamlit dashboard.
🎯 Business Problem
Amazon Kindle hosts millions of titles, yet reader abandonment remains high — not due to lack of content, but failed discovery. Readers leave the platform when they can't find their next book.
A high-performing recommendation engine directly addresses this by:
Reducing "no results found" drop-off in discovery flows
Increasing session engagement and purchase conversion
Replicating the same engine pattern Amazon credits with ~35% of its total revenue
PageMatch models this end-to-end: from raw relational data to a deployed, interactive recommendation product.
📊 Dataset
Attribute
Detail
Source
Amazon Kindle Ratings Dataset
Volume
520,000+ ratings across three relational tables
Tables
Books · Users · Ratings
Scope
Multi-table merge with ISBN matching, null handling, and deduplication
Filtered Cohort
900+ power readers (users with sufficient rating history)
🛠️ Tools & Technologies
Layer
Stack
Machine Learning
Python, Scikit-learn, k-Nearest Neighbours
Similarity Metric
Cosine Similarity on sparse user-item matrix
Data Engineering
Pandas, NumPy, pivot table construction
App & UI
Streamlit, Custom CSS (glassmorphism)
Deployment
Hugging Face Spaces (always-on, free tier)
Serialisation
Pickle — model + matrix + metadata bundled for <2s load time
Version Control
Git, GitHub
🔍 Key Analysis & Insights
Rating volume outperforms rating value as a signal. Filtering to power readers (high-frequency raters) before model fitting was the single largest driver of accuracy — eliminating cold-start noise that degrades most tutorial-level systems.
Publisher concentration creates a recommendation bias loop. A small subset of publishers account for a disproportionate share of high-rated books, systematically over-surfacing popular titles. Identified this as a structural fairness issue requiring correction in production systems.
Cosine similarity is the correct distance metric for sparse data. When most users have rated only a fraction of available titles, Euclidean distance collapses due to magnitude differences. Cosine similarity focuses on directional taste alignment — the industry-standard choice for sparse collaborative filtering (Netflix, Spotify, Amazon all use this pattern).
Book metadata is an underutilised signal layer. Genre, author, and series data remain outside the current model scope — a validated opportunity to extend toward a hybrid content + collaborative filtering system with meaningfully higher precision.
Cold-start threshold is a tunable hyperparameter, not a fixed rule. Calibrating the minimum ratings per user threshold directly controls the precision-recall trade-off — a design decision with measurable business consequences at scale.
📈 Key KPIs
Metric
Value
⭐ Ratings Processed
520,000+
👥 Power Reader Profiles
900+
🎯 Recall@10
95.76%
⚡ Recommendation Latency
< 2 seconds
🔍 Similarity Method
Cosine Similarity (k-NN)
🚀 Uptime
24/7 (Hugging Face Spaces)
💡 Business Impact
A 95.76% Recall@10 means at least one relevant recommendation surfaces in the top 10 results for nearly every query — directly reducing abandonment in a live discovery flow.
Filtering to power readers before model fitting eliminates cold-start degradation — a production-grade design decision that significantly improves signal quality over standard approaches.
The cosine similarity on a sparse pivot matrix is the same architectural pattern used by Netflix, Spotify, and Amazon at scale — making this directly transferable to e-commerce, streaming, and fintech personalisation pipelines.
Serialising the full pipeline (model + matrix + metadata) into a single deployable artefact achieves sub-2-second load times on a free cloud tier — demonstrating cost-efficient deployment thinking.
📷 Dashboard Preview
Book Search & Selection
Recommendation Results
�
Load image
�
Load image
Top Publishers Chart
Top Authors Chart
�
Load image
�
Load image
💡 For recruiters: Open the Live App, search any book title, and receive 5 personalised recommendations with cover images in under 2 seconds.
🚀 Conclusion
PageMatch demonstrates that a well-engineered recommendation system is an architecture and business decision problem — not just an algorithm selection. From handling sparse data at scale to making deliberate trade-offs on cold-start filtering and similarity metrics, every design choice maps directly to outcomes that matter in production: reduced churn, higher engagement, and faster discovery.
The system is live, fast, and built to the same standards used by consumer platforms at scale.
🔗 Project Links


🔴 Live App
Launch PageMatch on Hugging Face →
💻 Source Code
View Repository on GitHub →
👤 About
Ajaya Kumar Pradhan — Data Analyst | Power BI Developer | ML-Enabled Analytics
Builds end-to-end analytics and machine learning systems that connect raw data to real decisions — across SQL, Power BI, Python, and cloud deployment.
Python · Scikit-learn · Collaborative Filtering · SQL · Power BI · DAX · Streamlit · Feature Engineering
�
�
Load image
Load image
�
Personalisation at scale is an engineering discipline — not just an algorithm choice.


