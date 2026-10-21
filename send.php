<?php
// Hisab website: sends the "free site inspection" form to the company inbox.
// Replaces Netlify Forms now that the site is hosted on Hostinger.
$to = 'hvac@hisabtechnical.com';

if ($_SERVER['REQUEST_METHOD'] !== 'POST') { http_response_code(405); exit('Use the form on the contact page.'); }
if (!empty($_POST['bot-field'])) { http_response_code(200); exit('OK'); } // spam trap

function field($name, $max = 500) {
  $value = trim((string)($_POST[$name] ?? ''));
  return mb_substr(str_replace(["\r", "\0"], '', $value), 0, $max);
}

$name = field('name', 120);
$phone = field('phone', 40);
$email = filter_var(field('email', 120), FILTER_VALIDATE_EMAIL) ?: '';
$location = field('location', 200);
$message = field('message', 3000);
if ($name === '' || $phone === '' || $location === '' || $message === '') { http_response_code(400); exit('Please fill in the required fields.'); }

$lines = [
  'New site inspection request from hisabtechnical.com',
  '',
  'Name: ' . $name,
  'Mobile / WhatsApp: ' . $phone,
  'Email: ' . ($email ?: '-'),
  'Project location: ' . $location,
  'Project type: ' . field('project', 80),
  'AC system: ' . field('system', 40),
  'Project stage: ' . field('stage', 80),
  'Floors / rooms: ' . field('size', 120),
  'Google Maps link: ' . field('maplink', 500),
  '',
  'Message:',
  $message,
  '',
  'Sent on ' . gmdate('Y-m-d H:i') . ' UTC from ' . ($_SERVER['HTTP_REFERER'] ?? 'the website'),
];

$headers = [
  'From: Hisab website <website@hisabtechnical.com>',
  'Content-Type: text/plain; charset=UTF-8',
];
if ($email) $headers[] = 'Reply-To: ' . $email;

$subject = '=?UTF-8?B?' . base64_encode('New site inspection request: ' . $name) . '?=';
if (!mail($to, $subject, implode("\n", $lines), implode("\r\n", $headers))) {
  http_response_code(500);
  exit('Could not send.');
}
http_response_code(200);
echo 'OK';
