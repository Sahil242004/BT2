import json
import os
import urllib.error
import urllib.request


def json_rpc_call(rpc_url, method, params):
    payload = json.dumps(
        {
            "jsonrpc": "2.0",
            "id": 1,
            "method": method,
            "params": params,
        }
    ).encode("utf-8")

    req = urllib.request.Request(
        rpc_url,
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    with urllib.request.urlopen(req, timeout=20) as response:
        raw = response.read().decode("utf-8")
        parsed = json.loads(raw)

    if "error" in parsed:
        raise RuntimeError(parsed["error"])

    return parsed["result"]


def decode_string_abi(hex_data):
    data = hex_data[2:] if hex_data.startswith("0x") else hex_data
    if len(data) < 128:
        return ""

    length_hex = data[64:128]
    strlen = int(length_hex, 16)
    string_hex = data[128 : 128 + strlen * 2]
    return bytes.fromhex(string_hex).decode("utf-8", errors="replace")


def read_hello_message(rpc_url, contract_address):
    # Function selector for message() => 0xe21f37ce
    call_object = {
        "to": contract_address,
        "data": "0xe21f37ce",
    }
    result = json_rpc_call(rpc_url, "eth_call", [call_object, "latest"])
    return decode_string_abi(result)


def main():
    print("Assignment 10: Small DApp Client (Python JSON-RPC)")

    rpc_url = os.getenv("ETH_RPC_URL", "")
    contract_address = os.getenv("HELLOWORLD_CONTRACT", "")

    if not rpc_url or not contract_address:
        print("\nOffline demo mode")
        print("Set ETH_RPC_URL and HELLOWORLD_CONTRACT to query a deployed contract.")
        print("Example:")
        print("export ETH_RPC_URL='https://sepolia.infura.io/v3/YOUR_API_KEY'")
        print("export HELLOWORLD_CONTRACT='0xYourContractAddress'")
        return

    try:
        message = read_hello_message(rpc_url, contract_address)
        print("\nContract message():", message)
    except urllib.error.URLError as network_error:
        print("Network error:", network_error)
    except Exception as err:
        print("RPC/Decode error:", err)


if __name__ == "__main__":
    main()
