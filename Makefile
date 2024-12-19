# Define the Python interpreter
PYTHON = python3

# Target to run script1
run_script1:
	@if [ -z "$(files)" ]; then \
		echo "Usage: make run files=<value1>"; \
	else \
		$(PYTHON) ./scripts/script1.py $(files); \
	fi

# Target to run script2
run_script2:
	@if [ -z "$(files)" ]; then \
		echo "Usage: make run files=<value1>"; \
	else \
		$(PYTHON) ./scripts/script2.py $(files); \
	fi

# Target to run both scripts
run_scripts: run_script1 run_script2
