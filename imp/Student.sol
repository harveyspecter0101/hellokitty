pragma solidity ^0.8.0;

contract StudentData{

    struct student {
        uint roll_no;
        string name;
        uint marks;
    }

    student[] public students;

    function addStudent(uint roll,string memory n,uint m) public {
        students.push(student(roll,n,m));
    }

    function getStudent(uint index) public view returns(uint,string memory,uint) {
        require(index < students.length,"Out of Bound");
        student memory s = students[index];
        return (s.roll_no,s.name,s.marks);
    }

    function getTotal() public view returns(uint) {
        return students.length;
    }

    function editStudent(uint index,uint roll,string memory n,uint m) public {
        require(index < students.length,"Out of Bound");
        students[index].roll_no = roll;
        students[index].name = n;
        students[index].marks = m;
    }
}