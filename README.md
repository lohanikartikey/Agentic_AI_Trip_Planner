
## Running uvicorn

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

## Running streamlit

```bash
streamlit run streamlit_app.py
```
## uv environment

#### 1. Install uv
"""
pip install uv
"""
#### 2. Verify installation
"""
uv --version
"""

#### 3. Create a virtual environment
"""
uv venv
"""

#### 4. Activate the environment
"""
.venv\Scripts\activate
"""

#### 5. Install from requirements.txt
"""
uv pip install -r requirements.txt
"""
