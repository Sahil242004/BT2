import { network } from "hardhat";

async function main() {
  const cliSupply = process.argv.find((arg) => /^\d+$/.test(arg));
  const initialSupplyArg = process.env.INITIAL_SUPPLY || cliSupply || "1000000";
  const initialSupply = BigInt(initialSupplyArg);

  const { viem } = await network.connect();

  const contract = await viem.deployContract("SimpleToken", [initialSupply]);
  const deployer = (await viem.getWalletClients())[0].account.address;

  const totalSupply = await contract.read.totalSupply();
  const deployerBalance = await contract.read.balanceOf([deployer]);

  console.log("SimpleToken deployed at:", contract.address);
  console.log("Initial supply:", totalSupply.toString());
  console.log("Deployer:", deployer);
  console.log("Deployer balance:", deployerBalance.toString());
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
