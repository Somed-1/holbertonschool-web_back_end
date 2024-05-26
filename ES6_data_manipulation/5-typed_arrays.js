/* eslint-disable */

export default function createInt8TypedArray(length, position, num) {
  if (position >= length) {
    throw new Error("Position outside range");
  }

  let buffer = new ArrayBuffer(length);
  let view = new DataView(buffer);
  view.setInt8(position, num);

  return view;
}
