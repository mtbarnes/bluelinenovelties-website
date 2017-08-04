#! /bin/bash
find /backups/mysql/ -type f -mtime +14 -name '*.gz' -delete
