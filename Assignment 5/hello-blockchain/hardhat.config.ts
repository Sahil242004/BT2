import hardhatToolboxViemPlugin from "@nomicfoundation/hardhat-toolbox-viem";
import { configVariable, defineConfig } from "hardhat/config";

const sepoliaRpcUrl = process.env.SEPOLIA_RPC_URL ?? process.env.RPC_URL ?? configVariable("SEPOLIA_RPC_URL");
const rawPrivateKey = process.env.SEPOLIA_PRIVATE_KEY ?? process.env.PRIVATE_KEY;

function getSepoliaPrivateKey() {
  if (!rawPrivateKey || rawPrivateKey.includes("YOUR_PRIVATE_KEY")) {
    return configVariable("SEPOLIA_PRIVATE_KEY");
  }

  const normalized = rawPrivateKey.startsWith("0x") ? rawPrivateKey : `0x${rawPrivateKey}`;
  const isHexPrivateKey = /^0x[0-9a-fA-F]{64}$/.test(normalized);

  return isHexPrivateKey ? normalized : configVariable("SEPOLIA_PRIVATE_KEY");
}

const sepoliaPrivateKey = getSepoliaPrivateKey();

export default defineConfig({
  plugins: [hardhatToolboxViemPlugin],
  solidity: "0.8.28",
  networks: {
    sepolia: {
      type: "http",
      chainType: "l1",
      url: sepoliaRpcUrl,
      accounts: [sepoliaPrivateKey],
    },
  },
});