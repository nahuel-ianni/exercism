using System;
using System.Linq;
using System.Collections.Generic;

public class GradeSchool
{
    private readonly IList<(string Name, int Grade)> students = 
        new List<(string, int)>();

    public void Add(string student, int grade) =>
        students.Add((student, grade));

    public IEnumerable<string> Roster() =>
        students.OrderBy(x => x.Grade).ThenBy(x => x.Name).Select(x => x.Name);

    public IEnumerable<string> Grade(int grade) =>
        students.Where(x => x.Grade == grade).Select(x => x.Name).OrderBy(x => x);
}