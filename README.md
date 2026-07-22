# Cortex Code Hands-On Lab — Template

This is the generic template for generating city/domain-specific Cortex Code workshop labs. Each workshop is a Streamlit app that guides attendees through 6 sessions building an AI-powered operations platform on Snowflake.

## Workshop Structure

| Session | Topic | What's Built |
|---------|-------|--------------|
| 1 | Data Prep | Database, schema, warehouse, tables from CSV |
| 2 | Cortex Analyst & Semantic Views | Semantic view with relationships, metrics, natural language queries |
| 3 | Cortex Search | Knowledge base, search service, RAG pattern |
| 4 | Cortex Agents | Agent with Analyst + Search + custom UDF tools |
| 5 | CoWork | Collaborative AI data exploration |
| 6 | Streamlit | Operations dashboard with AI chat |

## Template Variables

All files use `{{VARIABLE_NAME}}` placeholders. When generating a new workshop, replace these with city/domain-specific values.

### Core Variables

| Variable | Description | Example (Calgary) | Example (Vancouver) |
|----------|-------------|-------------------|---------------------|
| `WORKSHOP_TITLE` | Main title | Alberta Energy Operations AI Workshop | Port of Vancouver AI Workshop |
| `WORKSHOP_SUBTITLE` | Subtitle line | Building Intelligence for Canada's Energy Sector... | Building Intelligence for Canada's Pacific Gateway... |
| `PAGE_ICON` | Streamlit page icon | `:material/oil_barrel:` | `:material/anchor:` |
| `SCENARIO_SHORT_NAME` | Short scenario name | Alberta Energy | Port of Vancouver |
| `SCENARIO_DESCRIPTION` | 2-3 sentence scenario intro | Alberta's oil sands and pipeline network... | The Port of Vancouver is Canada's largest port... |
| `DURATION` | Total workshop time | 2 hrs | 3 hrs |

### Event Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `EVENT_DATE` | Date string | July 16, 2026 |
| `EVENT_TIME_RANGE` | Time range | 9:00 AM to 11:00 AM |
| `VENUE_NAME` | Venue name | The Ampersant |
| `VENUE_CITY` | City/province | Calgary, AB |
| `SIGNUP_LINK` | Trial signup URL with tracking | https://signup.snowflake.com/?t=... |
| `ACCOUNT_LOCATOR_FORM_URL` | Google Form URL for account locator | https://docs.google.com/forms/... |
| `RECOMMENDED_REGION` | AWS region suggestion | AWS Canada (Central) or US West (Oregon) |

### Schedule Variables

| Variable | Description |
|----------|-------------|
| `TIME_ARRIVAL` | Arrival time slot |
| `TIME_WELCOME` | Welcome slot |
| `TIME_SESSION_1` through `TIME_SESSION_6` | Session time ranges |
| `TIME_BREAK` | Break time |
| `DUR_SESSION_1` through `DUR_SESSION_6` | Session durations |

### Data Variables

| Variable | Description | Example (Energy) |
|----------|-------------|------------------|
| `DATABASE_NAME` | Snowflake database | ENERGY_AI |
| `SCHEMA_NAME` | Schema name | OPS |
| `WAREHOUSE_NAME` | Warehouse name | ENERGY_WH |
| `NUM_TABLES` | Number of data tables | 9 |
| `TOTAL_ROWS` | Approximate total rows | 1,510 |
| `TABLE_LIST_UPPERCASE` | Comma-separated table names | FACILITIES, PIPELINES, PRODUCTION_RECORDS, ... |
| `TABLE_EXAMPLES` | Brief examples for agenda | Production records, pipeline throughput, safety incidents |
| `TABLE_DESCRIPTIONS_MARKDOWN` | Markdown table of all tables with descriptions | |
| `ZIP_FILENAME` | Name of the data zip file | energy_data.zip |
| `ZIP_DOWNLOAD_URL` | GitHub raw URL to the zip | https://github.com/.../energy_data.zip |
| `GITHUB_REPO` | Repository name | sfc-gh-obenning/coco-hol-calgary |

### Semantic View Variables

| Variable | Description |
|----------|-------------|
| `SEMANTIC_VIEW_NAME` | View name (e.g. ENERGY_OPERATIONS_VIEW) |
| `SEMANTIC_VIEW_TABLES` | Tables included in the view |
| `DIMENSION_TABLES` | Tables that are dimensions (have primary keys) |
| `RELATIONSHIPS_LIST` | Relationship descriptions |
| `FACTS_LIST` | Numeric fact columns |
| `DIMENSIONS_LIST` | Categorical dimension columns |
| `SYNONYMS_EXAMPLES` | Example synonym definitions |
| `METRICS_LIST` | Pre-defined metric calculations |
| `AI_INSTRUCTIONS_CONTEXT` | Domain context for AI_SQL_GENERATION |
| `DOMAIN_CONCEPTS_EXPLANATION` | Key domain concepts for explanation |
| `ANALYST_TEST_QUESTIONS` | 4 natural language test questions |
| `ANALYST_TEST_EXPLANATION` | Explanation of what each test validates |
| `SEMANTIC_VIEW_EXPANSION_INSTRUCTIONS` | Instructions for expanding the view |
| `EXPANSION_EXPLANATION` | Explanation of the expansion |

### Search & RAG Variables

| Variable | Description |
|----------|-------------|
| `KNOWLEDGE_BASE_TABLE` | Unified text table name |
| `KNOWLEDGE_BASE_UNION_INSTRUCTIONS` | SQL UNION definitions for each source |
| `SEARCH_SERVICE_NAME` | Cortex Search service name |
| `SEARCH_TEST_QUERIES` | 4 test search queries |
| `SEARCH_TEST_EXPLANATION` | What each search tests |
| `RAG_QUESTION` | The RAG demonstration question |

### Agent Variables

| Variable | Description |
|----------|-------------|
| `AGENT_NAME` | Agent object name |
| `AGENT_ROLE_DESCRIPTION` | Agent persona (e.g. "Alberta Energy Operations Assistant") |
| `AGENT_DOMAIN_CONTEXT` | Domain context for agent instructions |
| `STRUCTURED_QUESTION_TYPES` | Types of questions for Analyst tool |
| `UNSTRUCTURED_QUESTION_TYPES` | Types of questions for Search tool |
| `AGENT_TEST_QUERIES` | Test queries (structured, unstructured, mixed) |
| `CUSTOM_UDF_NAME` | Name of the custom UDF |
| `CUSTOM_UDF_SQL` | Full CREATE FUNCTION SQL |
| `CUSTOM_TOOL_TEST_QUESTION` | Test question for the custom tool |

### Streamlit Variables

| Variable | Description |
|----------|-------------|
| `STREAMLIT_APP_NAME` | App name (e.g. OPS_DASHBOARD) |
| `COMPUTE_POOL_NAME` | Compute pool name |
| `STREAMLIT_PAGE1_DESCRIPTION` | KPI cards, charts, tables for page 1 |

### CoWork Variables

| Variable | Description |
|----------|-------------|
| `COWORK_QUESTIONS` | Python list of (title, question) tuples |

## Generating a New Workshop

### Using the Cortex Code Skill

The recommended way to generate a new workshop is with the Cortex Code skill:

```
/generate-hol
```

This will prompt you for:
1. **City and venue** — Where is the workshop?
2. **Date and time** — When does it run?
3. **Domain/scenario** — What industry scenario? (ports, energy, healthcare, finance, etc.)
4. **Signup link** — Trial URL with tracking parameter
5. **GitHub repo** — Where to push the result

The skill will:
1. Copy this template
2. Generate domain-specific CSV data
3. Replace all `{{PLACEHOLDER}}` variables with scenario-appropriate content
4. Create the zip file
5. Commit and push to the target repo

### Manual Generation

1. Clone this template repo
2. Generate CSV data appropriate for your domain (see `data/` folder for structure)
3. Replace all `{{VARIABLE}}` placeholders in all `.py` files
4. Create a zip of the CSV files in `data/`
5. Copy CSVs to `static/` for web serving
6. Push to a new repo

## Deployment

### Streamlit Community Cloud

1. Push the completed workshop to a GitHub repo
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect the repo, point to `workshop_guide/streamlit_app.py`
4. Deploy

### Local Development

```bash
cd workshop_guide
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## File Structure

```
workshop_guide/
├── .streamlit/config.toml    # Theme and font configuration
├── app_pages/
│   ├── home.py               # Workshop overview and scenario
│   ├── getting_started.py    # Account provisioning steps
│   ├── agenda.py             # Schedule and deliverables
│   ├── session_01.py         # Data Prep
│   ├── session_02.py         # Cortex Analyst & Semantic Views
│   ├── session_03.py         # Cortex Search
│   ├── session_04.py         # Cortex Agents
│   ├── session_05.py         # CoWork
│   └── session_06.py         # Streamlit
├── data/                     # CSV files + zip
├── static/                   # Fonts, logos, CSV copies for serving
├── components.py             # Shared UI components
├── requirements.txt          # Python dependencies
└── streamlit_app.py          # Main entry point
```

## Previous Instances

| Date | City | Domain | Repo |
|------|------|--------|------|
| July 7, 2026 | Montreal | Port operations | sfc-gh-obenning/coco-hol-montreal |
| July 9, 2026 | Toronto | Port operations | sfc-gh-obenning/coco-hol-toronto |
| July 16, 2026 | Calgary | Energy/oil sands | sfc-gh-obenning/coco-hol-calgary |
| July 21, 2026 | Vancouver | Port operations | sfc-gh-obenning/coco-hol-vancouver |
