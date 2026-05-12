.PHONY: test-server test format mypy all

run-test-server:
	docker-compose up t212_mock_server --build --force-recreate

test:
	uv run python -m pytest tests

format:
	uv run black .
	uv run isort t212
	uv run isort tests

lint:
	uv run mypy .

