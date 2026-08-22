-- 初始化：本地直接执行本文件；Docker 首次启动会自动执行本文件
CREATE DATABASE IF NOT EXISTS todo_db DEFAULT CHARACTER SET utf8mb4;
USE todo_db;

CREATE TABLE IF NOT EXISTS users (
    id            INT AUTO_INCREMENT PRIMARY KEY,
    username      VARCHAR(50)  NOT NULL UNIQUE,   -- 唯一索引：注册时兜底防重名
    password_hash VARCHAR(100) NOT NULL,          -- "盐$哈希" 格式
    created_at    TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS todos (
    id         INT AUTO_INCREMENT PRIMARY KEY,
    user_id    INT NOT NULL,                      -- 这条 TODO 属于谁
    title      VARCHAR(200) NOT NULL,
    done       TINYINT(1) DEFAULT 0,              -- 0 未完成 / 1 已完成
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
