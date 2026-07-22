import streamlit as st
from components import render_session_header, render_prompt, render_explanation, render_technologies_used, render_key_concepts, render_what_you_built

render_session_header(6, "Streamlit", "{{TIME_SESSION_6}}", "{{DUR_SESSION_6}}", "Operations dashboard with AI chat interface")

render_technologies_used([
    {"name": "Streamlit in Snowflake (SiS)", "description": "Deploy Python-based data apps directly within Snowflake. Apps run on container runtime with full Python package support.", "icon": "web"},
    {"name": "Compute Pool", "description": "A managed pool of container nodes that powers SiS apps. Provides CPU/GPU resources and auto-scales.", "icon": "memory"},
    {"name": "st.connection(\"snowflake\")", "description": "The Streamlit connection API for Snowflake on container runtime. No credentials needed — inherits the logged-in user's session.", "icon": "terminal"},
])

st.markdown("---")

st.markdown("#### :material/open_in_new: Open Workspaces")
with st.container(border=True):
    st.markdown("""
For this section, open **Workspaces** in Snowsight (left navigation panel → Projects → Workspaces). Workspaces provides an IDE-like environment where Cortex Code can create and edit Streamlit app files directly.

Paste the prompts below into Cortex Code **within Workspaces** so the generated code is written directly into your app files.
""")


PROMPT_6_1 = """In {{DATABASE_NAME}}.{{SCHEMA_NAME}}, create a Streamlit app called {{STREAMLIT_APP_NAME}} that runs on the container runtime.

First, create a compute pool:
- Name: {{COMPUTE_POOL_NAME}}
- Use the CPU_X64_S instance family
- Min and max nodes of 1

Then create the Streamlit app with these 2 pages:

PAGE 1 - Operations Dashboard:
{{STREAMLIT_PAGE1_DESCRIPTION}}

PAGE 2 - Intelligence Chat:
- A chat interface using our {{AGENT_NAME}} via SNOWFLAKE.CORTEX.AGENT()
- Sidebar with summary stats from the data

Important for container runtime:
- Create an External Access Integration for pypi.org and files.pythonhosted.org
- Include a pyproject.toml with dependencies: ["streamlit[snowflake]>=1.50.0", "plotly"]
- Use st.connection("snowflake") for the connection
- Make it visually clean with st.columns

Execute all SQL."""

render_prompt("Prompt 6.1", "Create the Streamlit App", PROMPT_6_1)


PROMPT_6_2 = """Verify the Streamlit app and compute pool:

1. SHOW COMPUTE POOLS;
2. SHOW STREAMLITS IN SCHEMA {{DATABASE_NAME}}.{{SCHEMA_NAME}};
3. Describe the streamlit {{STREAMLIT_APP_NAME}};

Provide the direct URL to open the app in Snowsight."""

render_prompt("Prompt 6.2", "Verify & Access the App", PROMPT_6_2)

st.success("""
:material/rocket_launch: **Preview and Deploy your app!**

Once Cortex Code has generated your app files in Workspaces:

1. **Run** — Click the **Run** button (▶️) in the top-right of the Workspaces editor to preview your app.

2. **Deploy** — When happy with the preview, click **Deploy** to publish the app to your Snowflake account.

Try modifying the app (add a chart, change KPI labels) and re-run to see changes live!
""")

render_explanation("What this prompt does", """
Creates a full Streamlit in Snowflake application with an operations dashboard and AI chat connected to your {{AGENT_NAME}}.

This completes the workshop!
""")


render_key_concepts([
    {"term": "Container Runtime", "definition": "The current SiS execution environment. Apps run on a compute pool, support any Python package, and use versioned stage syntax."},
    {"term": "Compute Pool", "definition": "A managed pool of container nodes. Choose an instance family, set min/max nodes, and Snowflake handles provisioning."},
    {"term": "External Access Integration", "definition": "Required for container runtime apps that install pip packages. Must allow egress to pypi.org."},
])

render_what_you_built([
    "{{COMPUTE_POOL_NAME}} — compute pool for container runtime",
    "{{STREAMLIT_APP_NAME}} — 2-page Streamlit app",
    "Operations Dashboard with KPIs, charts, and data tables",
    "AI-powered chat interface connected to {{AGENT_NAME}}",
])
