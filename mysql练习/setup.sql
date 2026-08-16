-- 练习数据库：学生选课成绩系统（SQL 强化用）
DROP DATABASE IF EXISTS sql_practice;
CREATE DATABASE sql_practice DEFAULT CHARACTER SET utf8mb4;
USE sql_practice;

-- 班级表
CREATE TABLE classes (
    id INT PRIMARY KEY,
    name VARCHAR(20)
);

-- 学生表
CREATE TABLE students (
    id INT PRIMARY KEY,
    name VARCHAR(20),
    class_id INT,
    city VARCHAR(20),
    enroll_date DATE
);

-- 课程表
CREATE TABLE courses (
    id INT PRIMARY KEY,
    name VARCHAR(20),
    credit INT  -- 学分
);

-- 成绩表（多对多：一个学生选多门课）
CREATE TABLE scores (
    student_id INT,
    course_id INT,
    score INT
);

-- 插入数据
INSERT INTO classes VALUES (1, '软件1班'), (2, '软件2班'), (3, '网络1班');

INSERT INTO students VALUES
(1, '张三', 1, '北京', '2024-09-01'),
(2, '李四', 1, '上海', '2024-09-01'),
(3, '王五', 2, '北京', '2024-09-01'),
(4, '赵六', 2, '广州', '2024-09-02'),
(5, '孙七', 3, '深圳', '2024-09-02'),
(6, '周八', NULL, '杭州', '2024-09-03');  -- 注意：周八没分班

INSERT INTO courses VALUES
(1, '高等数学', 4),
(2, '数据库原理', 3),
(3, 'Python编程', 2),
(4, '大学英语', 3);

INSERT INTO scores VALUES
(1, 1, 85), (1, 2, 92), (1, 3, 88),
(2, 1, 76), (2, 2, 81), (2, 3, 95), (2, 4, 72),
(3, 1, 91), (3, 2, 78),
(4, 2, 65), (4, 3, 58),              -- 赵六：数据库65，Python挂科
(5, 1, 55), (5, 4, 89),              -- 孙七：高数挂科
(6, 3, 97);                          -- 周八：只选了Python

SELECT '数据准备完成' AS 状态;
