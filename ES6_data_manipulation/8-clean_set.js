/* eslint-disable */

export default function cleanSet(set, startString = "") {
  const str = [];

  if (startString.length === 0) {
    return "";
  }

  for (const item of set) {
    if (item && item.startsWith(startString)) {
      str.push(item.slice(startString.length));
    }
  }

  return str.join("-");
}
