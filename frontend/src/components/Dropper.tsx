// Dropper.tsx
import React, { useEffect, useState } from 'react';
import { Group, Text, Notification, rem, Loader, Center } from '@mantine/core';
import { IconUpload, IconPhoto, IconX, IconCheck } from '@tabler/icons-react';
import { Dropzone, DropzoneProps, IMAGE_MIME_TYPE } from '@mantine/dropzone';
import { useAppDispatch, useAppSelector } from '../hooks';
import { uploadFile, setError } from '../features/imgSlice';
import Grepper from "./Grepper"


export default function Dropper(props: Partial<DropzoneProps>) {
  const dispatch = useAppDispatch();
  const { error, extractedText, loading } = useAppSelector((state) => state.upload);

  const [showErrorNotification, setShowErrorNotification] = useState(false);
  const [hasExtracted, setHasExtracted] = useState(false)

  const handleDrop = (files: File[]) => {
    if (files.length > 0) {
      dispatch(uploadFile(files[0]));
      setHasExtracted(true)
    }
  };

  const handleReject = () => {
    dispatch(setError('File rejected'));
    setShowErrorNotification(true);
  };

  // NOTIFCATIONS

  useEffect(() => {
    if (showErrorNotification) {
      const timer = setTimeout(() => {
        setShowErrorNotification(false);
      }, 3000);

      return () => clearTimeout(timer);
    }
  }, [showErrorNotification]);

  const xIcon = <IconX style={{ width: rem(20), height: rem(20) }} />;

  return (
    <>
      <Grepper shouldReplaceText={hasExtracted} extractedText={extractedText}/>
      <div>
        <Dropzone
          onDrop={handleDrop}
          onReject={handleReject}
          maxSize={5 * 1024 ** 2}
          accept={IMAGE_MIME_TYPE}
          maxFiles={1}
          {...props}
          style = {{ cursor: 'pointer' }}
        >
          
          <Group justify="center" gap="xl" mih={220}>
            <Dropzone.Accept>
              <IconUpload
                style={{ width: rem(52), height: rem(52), color: 'var(--mantine-color-blue-6)' }}
                stroke={1.5}
              />
            </Dropzone.Accept>
            <Dropzone.Reject>
              <IconX
                style={{ width: rem(52), height: rem(52), color: 'var(--mantine-color-red-6)' }}
                stroke={1.5}
              />
            </Dropzone.Reject>
            <Dropzone.Idle>
              <IconPhoto
                style={{ width: rem(52), height: rem(52), color: 'var(--mantine-color-dimmed)' }}
                stroke={1.5}
              />
            </Dropzone.Idle>

            <div>
              <Text size="md" inline>
                Get your string from an image.
              </Text>
              <Text size="xs" c="dimmed" inline mt={7}>
                Drag and drop your image here or click to select a file.
              </Text>
            </div>
          </Group>
        </Dropzone>

        {loading && <Center><Loader color="violet" /></Center>}
        {/* {extractedText && (
          <div style={{ marginTop: '20px' }}>
            <Text size="md">Extracted Text:</Text>
            <Text size="sm">{extractedText}</Text>
          </div>
        )} */}
      </div>

      {showErrorNotification && (
        <Notification
          icon={xIcon}
          color="red"
          title="File upload failed!"
          onClose={() => setShowErrorNotification(false)}
          // disallowClose={false}
        >
          Please try uploading only one file at a time or limit the file size.
        </Notification>
      )}

      {/* Add any success notification logic similarly if needed */}
    </>
  );
}