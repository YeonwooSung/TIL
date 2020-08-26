# PM2 Commands

## Installation

Using node package manager(npm), you can install PM2 on the server.

```bash
npm install pm2 -g
```

This package should be installed as a global node.

## Usage

### Start

PM2 is having the simplest command to start, daemonize and monitor your application.

```bash
pm2 start index.js
```

The command above starts the service of "index.js".

#### Advanced

```bash
pm2 start index.js -i <id> --name "<name>"
```

### List

Using below command, you can display all the processes with status.

```bash
pm2 list
```

### Stop

To stop an application, you can use below command.

```bash
pm2 stop <id|name>
```

#### Stop all

``` bash
pm2 stop all
```

### Restart

Restart the previous app launched by name

```bash
pm2 restart <id|name>
```

#### Restart all

```bash
pm2 restart all
```

### Delete

Stop and delete a process from pm2 process list

```bash
pm2 delete <id|name>
```

#### Delete all

```bash
pm2 delete all
```

### Details

To get more details about an application

```bash
pm2 show <id|name>
```

### Monitor

To monitor the resource usage of your application

```bash
pm2 monit

pm2 monit <id|name>
```

### Kill

To stop the PM2

```bash
pm2 kill
```

### Logs

Your application logs are stored into server hard disk.

```bash
pm2 logs
```
