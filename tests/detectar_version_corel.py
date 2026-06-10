import win32com.client

try:

    app = win32com.client.Dispatch(
        "CorelDRAW.Application"
    )

    print("✅ Corel detectado")

except Exception as e:

    print("❌ Error:", e)