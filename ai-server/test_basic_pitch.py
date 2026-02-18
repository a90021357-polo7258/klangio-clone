
import sys
print(f"Python version: {sys.version}")

try:
    print("Attempting to import basic_pitch...")
    from basic_pitch.inference import predict
    print("SUCCESS: basic_pitch imported successfully.")
except ImportError as e:
    print(f"ERROR: ImportError during basic_pitch import: {e}")
except Exception as e:
    print(f"ERROR: Unexpected error during basic_pitch import: {e}")

try:
    import tensorflow as tf
    print(f"TensorFlow version: {tf.__version__}")
except ImportError as e:
    print(f"ERROR: TensorFlow import failed: {e}")

print("Test complete.")
