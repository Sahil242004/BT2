import { network } from "hardhat";

async function main() {
  const addressArgs = process.argv.filter((arg) => /^0x[0-9a-fA-F]{40}$/.test(arg));
  const numericArg = process.argv.find((arg) => /^\d+$/.test(arg));

  const tokenAddress = process.env.TOKEN_ADDRESS || addressArgs[0];
  const receiverAddress = process.env.TRANSFER_TO || addressArgs[1];
  const amountArg = process.env.TRANSFER_AMOUNT || numericArg || "1";

  if (!tokenAddress || !receiverAddress) {
    throw new Error("Usage: npx hardhat run --network sepolia scripts/transfer-simple-token.js -- <tokenAddress> <receiverAddress> <amount>");
  }

  const amount = BigInt(amountArg);
  const { viem } = await network.connect();
  const [walletClient] = await viem.getWalletClients();
  const publicClient = await viem.getPublicClient();
  const senderAddress = walletClient.account.address;

  const token = await viem.getContractAt("SimpleToken", tokenAddress);

  const senderBefore = await token.read.balanceOf([senderAddress]);
  const receiverBefore = await token.read.balanceOf([receiverAddress]);

  console.log("Sender before:", senderBefore.toString());
  console.log("Receiver before:", receiverBefore.toString());

  const txHash = await token.write.transfer([receiverAddress, amount], {
    account: walletClient.account,
  });

  console.log("Transfer tx hash:", txHash);
  await publicClient.waitForTransactionReceipt({ hash: txHash });

  const senderAfter = await token.read.balanceOf([senderAddress]);
  const receiverAfter = await token.read.balanceOf([receiverAddress]);

  console.log("Sender after:", senderAfter.toString());
  console.log("Receiver after:", receiverAfter.toString());
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
