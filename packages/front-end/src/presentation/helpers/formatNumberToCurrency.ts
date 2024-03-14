export function formatNumberToCurrency(value: number) {
  return value.toLocaleString("en-US", {
    minimumFractionDigits: 2,
    style: "currency",
    currency: "USD",
  });
}