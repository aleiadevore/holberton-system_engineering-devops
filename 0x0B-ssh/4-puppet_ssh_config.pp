# Changes permissions to refuse password
class { 'ssh'
      server_options => {
        'PasswordAuthentication' => 'no',
  'ChallengeResponseAuthentication' => 'no'
  'UsePAM' => 'no'
      }
}