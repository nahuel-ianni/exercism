using System.Linq;
using System.Collections.Generic;

public class GradeSchool
{
    private List<(string Name, int Grade)> students = 
        new List<(string Name, int Grade)>();

    public void Add(string student, int grade)
    {
        students.Add((student, grade));
        students.Sort((x, y) => x.Grade == y.Grade
            ? string.Compare(x.Name, y.Name)
            : x.Grade.CompareTo(y.Grade));
    }

    public IEnumerable<string> Roster() =>
        students.Select(x => x.Name);

    public IEnumerable<string> Grade(int grade) =>
        students.Where(x => x.Grade == grade).Select(x => x.Name);
}