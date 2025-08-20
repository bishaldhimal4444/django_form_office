# django_form_office

<h1>SSH Agent Forwarding</h1>
<br>
1. Start ssh agent:
```
eval "$(ssh-agent -s)"
```
<br>
2. Add your key:
```
locate your bastion_host pem file: pwd
```
<br>
```
ssh-add /path/to/your/*.pem
```
<br>
3. Connect to the bastion host with agent forwarding:
<br>
```
ssh -A ubuntu@<instance_ip>.compute-1.amazonaws.com
```
