import subprocess


def run_ettercap(interface: str):
    try:
        command = ["sudo", "ettercap", "-T", "-i", interface]

        process = subprocess.Popen(
            command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )
        stdout, stderr = process.communicate()

        if stderr:
            print(f"Error: {stderr}")

        return dict(
            {"stdout": stdout, "investigation_result": investigate_mitm(stdout)}
        )
    except Exception as e:
        print(f"Exception: {e}")


def investigate_mitm(stdout):
    alert_keywords = ["ARP poisoning detected", "WARNING", "MITM attack"]

    vulnerability_list = []
    for line in stdout.split("\n"):
        if any(keyword in line for keyword in alert_keywords):
            print("[ALERT] Possible MITM attack detected!")
            print(line)  # Log the suspicious activity
            vulnerability_list.append(line)

        return vulnerability_list
