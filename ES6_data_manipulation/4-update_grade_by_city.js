/* eslint-disable */

export default function updateStudentGradeByCity(array, city, newGrade) {
  if (!Array.isArray(array)) return [];
  return array
    .filter((student) => student.location === city)
    .map((student) => {
      const [int] = newGrade.filter((grade) => grade.studentId === student.id);
      return {
        ...student,
        grade: int ? int.grade : "N/A",
      };
    });
}
