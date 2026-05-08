import hre from "hardhat";

async function main() {
  const initialMessage = process.argv[2] || "Hello from Assignment 5";

  const contract = await hre.viem.deployContract("HelloWorld", [
    initialMessage,
  ]);

  const currentMessage = await contract.read.message();

  console.log("HelloWorld deployed at:", contract.address);
  console.log("Initial message:", currentMessage);
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});