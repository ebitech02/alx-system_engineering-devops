# testing

exec { 'nofile hard_limit':
    command =>  'sed -i "/^.*soft nofile/s/^[^#]*$/* soft nofile 10000/" /etc/security/limits.conf && \
    sed -i "/^.*hard nofile/s/^[^#]*$/* hard nofile 10000/" /etc/security/limits.conf',
    path    =>  '/bin:/usr/bin',
    }