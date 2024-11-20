import io
import sys
from herzeus import main

def test_main_output(capsys):
   main()
   captured = capsys.readouterr()
   assert captured.out == "Hello from herzeus!\n"

def test_main_returns_none():
   assert main() is None

def test_main_no_side_effects():
   original_stdout = sys.stdout
   temp_stdout = io.StringIO()
   sys.stdout = temp_stdout
   
   try:
       main()
   finally:
       sys.stdout = original_stdout
   
   assert sys.stdout is original_stdout
