#!/usr/bin/node
const number = parseInt(process.argv[2]);
if (!number) console.log('Missing size');
else {
  let v = '';
  for (let i = 0; i < number; i++) v += 'x';
  v.split('').forEach(() => console.log(v));
}
