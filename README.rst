shodawn
=======
white hat opportunity to inform sys-admins that their servers are vulnerable via some shodan recon of redis and mongodb ports

inspiration
^^^^^^^^^^^
`It's still the data stupid`__

requirements
^^^^^^^^^^^^
python 3+ - no more coddling those who haven't upgraded, stop whining.
pip package shodan via ``sudo pip3 install shodan``
pip package redis via ``sudo pip3 install redis``

place configs.py file with a variable called apikey that is your shodan key into the same directory you clone this to.

.. __: https://blog.shodan.io/its-still-the-data-stupid/

quickstart
^^^^^^^^^^
1. git clone this repo.
2. run test_connect_to_shodan.py to confirm everything is working.
3. run python3 shodawn.py and follow prompts using two letter country code for recon location

roadmap
^^^^^^^
1. add mongodb recon
2. add postgres recon
3. add mysql recon
4. add geo-filter query (shodan accepts lat,long and radius)
5. add auto-email the owners of the servers that they have open databases and that they need to lock it down

recommendations to lock down your server
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
1. use ufw. ``sudo apt-get install ufw or sudo yum install ufw`` add first rule ``sudo ufw default deny all`` then allow as needed, eg ``sudo ufw allow 80,443`` then ``sudo ufw enable``
2. use fail2ban ``sudo apt-get install fail2ban``
