
import warnings
warnings.warn("Test error")
try:
    n = [0]
    print(n[2])
    n = float("1,25")
except ValueError:
    print("Value error")
except IndexError:
    print("Index")
except:
    print("Error")

print("End program")
