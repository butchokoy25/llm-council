FROM python:3.11-slim

WORKDIR /app

# Install uv
RUN pip install uv

# Copy dependencies
COPY pyproject.toml uv.lock ./

# Install dependencies
RUN uv sync --frozen

# Copy application code
COPY backend ./backend
COPY README.md .

# Create data directory
RUN mkdir -p data/conversations

# Run the app
# Use uv run to ensure we use the virtual environment created by sync
CMD ["uv", "run", "python", "-m", "backend.main"]
