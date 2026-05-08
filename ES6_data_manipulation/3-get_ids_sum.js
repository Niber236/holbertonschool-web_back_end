export default function getIdsSum(students) {
  return students.reduce((accumulator, currentValue) => accumulator + currentValue.id, 0);
}