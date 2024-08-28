import { createQueue } from 'kue';

const queue = createQueue();
const jobData = { phoneNumber: '+25497711372', message: 'MESSAGE: Received notification from kue->queue.create' };
const job = queue.create('push_notification_code', jobData).save((error) => {
  if (!error) console.log(`Notification job created: ${job.id}`);
});

job.on('complete', () => console.log('Notification job completed'));
job.on('failed', () => console.log('Notification job failed'));
