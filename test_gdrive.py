import sys
sys.path.insert(0, 'dist/SteaMidra_GUI/_internal')

from sff.cloud.google_drive import is_available, is_authenticated, authorize, _client_config

print("Testing Google Drive...")
print(f"_client_config(): {_client_config()}")
print(f"is_available(): {is_available()}")
print(f"is_authenticated(): {is_authenticated()}")

if is_available():
    print("Google Drive is available, testing authorize...")
    log_lines = []
    ok = authorize(log_func=log_lines.append)
    print(f"Authorize result: {ok}")
    print("Log lines:")
    for line in log_lines:
        print(f"  {line}")
else:
    print("Google Drive NOT available")
    # Check imports
    try:
        import google.auth
        print("google.auth: OK")
    except ImportError as e:
        print(f"google.auth: FAILED - {e}")
    try:
        import google_auth_oauthlib
        print("google_auth_oauthlib: OK")
    except ImportError as e:
        print(f"google_auth_oauthlib: FAILED - {e}")
    try:
        import googleapiclient
        print("googleapiclient: OK")
    except ImportError as e:
        print(f"googleapiclient: FAILED - {e}")